"""Riddlewood Pin Scheduler — Web Dashboard.

Flask app that demonstrates Pinterest API integration with OAuth2 flow,
board management, and pin creation. Built to satisfy Pinterest Standard
access review requirements (real UI + real OAuth + real API calls).

Run:  .venv/bin/python automation/pinterest/web_dashboard.py
Open: http://localhost:3004
"""
from __future__ import annotations

import base64
import json
import secrets
import time
import urllib.parse
from pathlib import Path

import requests
from flask import Flask, redirect, render_template, request, session, url_for

HERE = Path(__file__).resolve().parent
ENV_PATH = HERE / ".env"
TOKEN_PATH = HERE / "token.json"

AUTH_URL = "https://www.pinterest.com/oauth/"
TOKEN_URL = "https://api.pinterest.com/v5/oauth/token"
API_BASE = "https://api.pinterest.com/v5"
SCOPES = "boards:read,boards:write,pins:read,pins:write,user_accounts:read"


def load_env() -> dict:
    if not ENV_PATH.exists():
        raise SystemExit(f"Missing {ENV_PATH}")
    env: dict[str, str] = {}
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


ENV = load_env()
app = Flask(__name__, template_folder=str(HERE / "templates"))
app.secret_key = secrets.token_hex(32)


# ── API helpers ──────────────────────────────────────────────────────

def _get_token() -> dict | None:
    if TOKEN_PATH.exists():
        return json.loads(TOKEN_PATH.read_text())
    return None


def _save_token(tok: dict):
    TOKEN_PATH.write_text(json.dumps(tok, indent=2))


def _refresh_if_needed(tok: dict) -> dict:
    if time.time() < tok.get("expires_at", 0):
        return tok
    creds = base64.b64encode(
        f"{ENV['PINTEREST_APP_ID']}:{ENV['PINTEREST_APP_SECRET']}".encode()
    ).decode()
    resp = requests.post(TOKEN_URL, data={
        "grant_type": "refresh_token",
        "refresh_token": tok["refresh_token"],
    }, headers={
        "Authorization": f"Basic {creds}",
        "Content-Type": "application/x-www-form-urlencoded",
    }, timeout=30)
    resp.raise_for_status()
    tok = resp.json()
    tok["expires_at"] = time.time() + tok.get("expires_in", 3600) - 60
    _save_token(tok)
    return tok


def api_get(path: str, tok: dict) -> dict:
    tok = _refresh_if_needed(tok)
    resp = requests.get(
        f"{API_BASE}{path}",
        headers={"Authorization": f"Bearer {tok['access_token']}"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def api_post(path: str, tok: dict, payload: dict) -> dict:
    tok = _refresh_if_needed(tok)
    resp = requests.post(
        f"{API_BASE}{path}",
        headers={"Authorization": f"Bearer {tok['access_token']}"},
        json=payload,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


# ── Routes ───────────────────────────────────────────────────────────

@app.route("/")
def index():
    tok = _get_token()
    if tok:
        try:
            tok = _refresh_if_needed(tok)
            user = api_get("/user_account", tok)
            return redirect(url_for("dashboard"))
        except Exception:
            pass
    return render_template("landing.html")


@app.route("/connect")
def connect():
    state = secrets.token_urlsafe(16)
    session["oauth_state"] = state
    qs = urllib.parse.urlencode({
        "client_id": ENV["PINTEREST_APP_ID"],
        "redirect_uri": ENV["PINTEREST_REDIRECT_URI"],
        "response_type": "code",
        "scope": SCOPES,
        "state": state,
    })
    return redirect(f"{AUTH_URL}?{qs}")


@app.route("/callback")
def callback():
    code = request.args.get("code")
    state = request.args.get("state")

    if not code:
        return render_template("error.html", message="Authorization cancelled or failed."), 400

    creds = base64.b64encode(
        f"{ENV['PINTEREST_APP_ID']}:{ENV['PINTEREST_APP_SECRET']}".encode()
    ).decode()
    resp = requests.post(TOKEN_URL, data={
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": ENV["PINTEREST_REDIRECT_URI"],
    }, headers={
        "Authorization": f"Basic {creds}",
        "Content-Type": "application/x-www-form-urlencoded",
    }, timeout=30)

    if resp.status_code >= 400:
        return render_template("error.html", message=f"Token exchange failed: {resp.text}"), 400

    tok = resp.json()
    tok["expires_at"] = time.time() + tok.get("expires_in", 3600) - 60
    _save_token(tok)
    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():
    tok = _get_token()
    if not tok:
        return redirect(url_for("index"))

    try:
        tok = _refresh_if_needed(tok)
        user = api_get("/user_account", tok)
        boards_data = api_get("/boards?page_size=25", tok)
        boards = boards_data.get("items", [])
        pins_data = api_get("/pins?page_size=20", tok)
        pins = pins_data.get("items", [])
    except Exception as e:
        return render_template("error.html", message=str(e))

    return render_template("dashboard.html", user=user, boards=boards, pins=pins)


@app.route("/boards")
def boards_page():
    tok = _get_token()
    if not tok:
        return redirect(url_for("index"))
    try:
        tok = _refresh_if_needed(tok)
        boards_data = api_get("/boards?page_size=25", tok)
        boards = boards_data.get("items", [])
    except Exception as e:
        return render_template("error.html", message=str(e))
    return render_template("boards.html", boards=boards)


@app.route("/create-pin", methods=["GET", "POST"])
def create_pin():
    tok = _get_token()
    if not tok:
        return redirect(url_for("index"))

    try:
        tok = _refresh_if_needed(tok)
        boards_data = api_get("/boards?page_size=25", tok)
        boards = boards_data.get("items", [])
    except Exception as e:
        return render_template("error.html", message=str(e))

    if request.method == "POST":
        board_id = request.form.get("board_id")
        title = request.form.get("title", "")
        description = request.form.get("description", "")
        link = request.form.get("link", "")
        image_file = request.files.get("image")

        if not board_id or not image_file:
            return render_template("create_pin.html", boards=boards,
                                   error="Board and image are required.")

        img_bytes = image_file.read()
        b64 = base64.b64encode(img_bytes).decode()
        ext = image_file.filename.rsplit(".", 1)[-1].lower() if image_file.filename else "png"
        ct = "image/png" if ext == "png" else "image/jpeg"

        payload = {
            "board_id": board_id,
            "title": title[:100],
            "description": description[:500],
            "media_source": {
                "source_type": "image_base64",
                "content_type": ct,
                "data": b64,
            },
        }
        if link:
            payload["link"] = link

        try:
            result = api_post("/pins", tok, payload)
            return render_template("pin_created.html", pin=result)
        except Exception as e:
            error_msg = str(e)
            if "403" in error_msg:
                error_msg = "Pin creation requires Standard access (currently Trial). The API returned 403 — upgrade needed."
            return render_template("create_pin.html", boards=boards, error=error_msg)

    return render_template("create_pin.html", boards=boards, error=None)


@app.route("/disconnect")
def disconnect():
    if TOKEN_PATH.exists():
        TOKEN_PATH.unlink()
    return redirect(url_for("index"))


if __name__ == "__main__":
    print("\n  Riddlewood Pin Scheduler")
    print(f"  Open http://localhost:3004\n")
    app.run(host="localhost", port=3004, debug=False)
