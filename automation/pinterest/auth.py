"""Pinterest OAuth2 — one-time authorize + token store.

Reads credentials from automation/pinterest/.env, opens the Pinterest consent
page, catches the redirect on localhost, exchanges the code for tokens, and
writes token.json (with refresh support used by pinterest_client.py).

Run (after .env is filled and the Pinterest app is created):
    .venv/bin/python automation/pinterest/auth.py
"""
from __future__ import annotations

import base64
import http.server
import json
import os
import secrets
import threading
import time
import urllib.parse
import webbrowser
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
ENV_PATH = HERE / ".env"
TOKEN_PATH = HERE / "token.json"

AUTH_URL = "https://www.pinterest.com/oauth/"
TOKEN_URL = "https://api.pinterest.com/v5/oauth/token"
SCOPES = "boards:read,boards:write,pins:read,pins:write,user_accounts:read"


def load_env() -> dict:
    if not ENV_PATH.exists():
        raise SystemExit(f"Missing {ENV_PATH}. Copy .env.example to .env and fill it.")
    env: dict[str, str] = {}
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    for required in ("PINTEREST_APP_ID", "PINTEREST_APP_SECRET", "PINTEREST_REDIRECT_URI"):
        if not env.get(required):
            raise SystemExit(f"{required} not set in {ENV_PATH}")
    return env


class _CallbackHandler(http.server.BaseHTTPRequestHandler):
    captured: dict = {}

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if "callback" in parsed.path:
            params = urllib.parse.parse_qs(parsed.query)
            _CallbackHandler.captured = {k: v[0] for k, v in params.items()}
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>Pinterest authorized. You can close this tab.</h2>")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, *args):
        pass


def authorize() -> dict:
    env = load_env()
    state = secrets.token_urlsafe(16)
    redirect_uri = env["PINTEREST_REDIRECT_URI"]
    parsed = urllib.parse.urlparse(redirect_uri)
    host, port = parsed.hostname or "localhost", parsed.port or 3004

    qs = urllib.parse.urlencode({
        "client_id": env["PINTEREST_APP_ID"],
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": SCOPES,
        "state": state,
    })
    url = f"{AUTH_URL}?{qs}"

    server = http.server.HTTPServer((host, port), _CallbackHandler)
    t = threading.Thread(target=server.handle_request)
    t.start()
    print("Opening Pinterest authorization page in your browser...")
    print(f"If it doesn't open, paste this URL:\n{url}\n")
    webbrowser.open(url)
    t.join(timeout=300)
    server.server_close()

    captured = _CallbackHandler.captured
    if captured.get("state") != state or "code" not in captured:
        raise SystemExit(f"Authorization failed or timed out. Got: {captured}")

    creds = base64.b64encode(
        f"{env['PINTEREST_APP_ID']}:{env['PINTEREST_APP_SECRET']}".encode()
    ).decode()
    resp = requests.post(TOKEN_URL, data={
        "grant_type": "authorization_code",
        "code": captured["code"],
        "redirect_uri": redirect_uri,
    }, headers={
        "Authorization": f"Basic {creds}",
        "Content-Type": "application/x-www-form-urlencoded",
    }, timeout=30)
    resp.raise_for_status()
    tok = resp.json()
    tok["expires_at"] = time.time() + tok.get("expires_in", 3600) - 60
    TOKEN_PATH.write_text(json.dumps(tok, indent=2))
    print(f"Success. Token saved to {TOKEN_PATH}")
    return tok


if __name__ == "__main__":
    authorize()
