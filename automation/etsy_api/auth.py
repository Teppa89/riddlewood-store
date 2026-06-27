"""Etsy OAuth2 (Authorization Code + PKCE) — one-time authorize + token store.

Reads credentials from automation/etsy_api/.env, opens the Etsy consent page,
catches the redirect on localhost, exchanges the code for tokens, and writes
token.json (with refresh support used by etsy_client.py).

Run (after .env is filled and the Etsy app is approved):
    .venv/bin/python automation/etsy_api/auth.py
"""
from __future__ import annotations

import base64
import hashlib
import http.server
import json
import os
import secrets
import threading
import urllib.parse
import webbrowser
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
ENV_PATH = HERE / ".env"
TOKEN_PATH = HERE / "token.json"

AUTH_URL = "https://www.etsy.com/oauth/connect"
TOKEN_URL = "https://api.etsy.com/v3/public/oauth/token"
SCOPES = "listings_r listings_w email_r shops_r"


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
    for required in ("ETSY_KEYSTRING", "ETSY_SHARED_SECRET", "ETSY_REDIRECT_URI"):
        if not env.get(required):
            raise SystemExit(f"{required} not set in {ENV_PATH}")
    return env


def pkce_pair() -> tuple[str, str]:
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(48)).rstrip(b"=").decode()
    challenge = base64.urlsafe_b64encode(
        hashlib.sha256(verifier.encode()).digest()
    ).rstrip(b"=").decode()
    return verifier, challenge


class _CallbackHandler(http.server.BaseHTTPRequestHandler):
    captured: dict = {}

    def do_GET(self):  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path.split("?")[0].rstrip("/").endswith("callback") or parsed.path.startswith("/callback"):
            params = urllib.parse.parse_qs(parsed.query)
            _CallbackHandler.captured = {k: v[0] for k, v in params.items()}
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>Etsy authorized. You can close this tab.</h2>")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, *args):  # silence
        pass


def authorize() -> dict:
    env = load_env()
    verifier, challenge = pkce_pair()
    state = secrets.token_urlsafe(16)
    redirect_uri = env["ETSY_REDIRECT_URI"]
    parsed = urllib.parse.urlparse(redirect_uri)
    host, port = parsed.hostname or "localhost", parsed.port or 3003

    qs = urllib.parse.urlencode({
        "response_type": "code",
        "client_id": env["ETSY_KEYSTRING"],
        "redirect_uri": redirect_uri,
        "scope": SCOPES,
        "state": state,
        "code_challenge": challenge,
        "code_challenge_method": "S256",
    })
    url = f"{AUTH_URL}?{qs}"

    server = http.server.HTTPServer((host, port), _CallbackHandler)
    t = threading.Thread(target=server.handle_request)  # serve one request
    t.start()
    print("Opening Etsy authorization page in your browser...")
    print(f"If it doesn't open, paste this URL:\n{url}\n")
    webbrowser.open(url)
    t.join(timeout=300)
    server.server_close()

    captured = _CallbackHandler.captured
    if captured.get("state") != state or "code" not in captured:
        raise SystemExit(f"Authorization failed or timed out. Got: {captured}")

    resp = requests.post(TOKEN_URL, data={
        "grant_type": "authorization_code",
        "client_id": env["ETSY_KEYSTRING"],
        "redirect_uri": redirect_uri,
        "code": captured["code"],
        "code_verifier": verifier,
    }, timeout=30)
    resp.raise_for_status()
    tok = resp.json()
    import time
    tok["expires_at"] = time.time() + tok.get("expires_in", 3600) - 60
    TOKEN_PATH.write_text(json.dumps(tok, indent=2))
    print(f"Success. Token saved to {TOKEN_PATH}")
    # access_token format is "<user_id>.<random>" — surface the user_id
    uid = tok.get("access_token", "").split(".")[0]
    print(f"Authorized user_id: {uid}")
    return tok


if __name__ == "__main__":
    authorize()
