"""Pinterest API v5 client — create pins, manage boards, auto-refresh tokens.

Mirrors the pattern from etsy_client.py. Requires a registered Pinterest app
with pins:write and boards:read scopes.
"""
from __future__ import annotations

import base64
import json
import time
from pathlib import Path

import requests

from auth import load_env, TOKEN_PATH, TOKEN_URL

API_BASE = "https://api.pinterest.com/v5"


class PinterestClient:
    def __init__(self):
        self.env = load_env()
        if not TOKEN_PATH.exists():
            raise SystemExit(f"No {TOKEN_PATH}. Run auth.py first.")
        self.token = json.loads(TOKEN_PATH.read_text())

    def _refresh_if_needed(self):
        if time.time() < self.token.get("expires_at", 0):
            return
        creds = base64.b64encode(
            f"{self.env['PINTEREST_APP_ID']}:{self.env['PINTEREST_APP_SECRET']}".encode()
        ).decode()
        resp = requests.post(TOKEN_URL, data={
            "grant_type": "refresh_token",
            "refresh_token": self.token["refresh_token"],
        }, headers={
            "Authorization": f"Basic {creds}",
            "Content-Type": "application/x-www-form-urlencoded",
        }, timeout=30)
        resp.raise_for_status()
        self.token = resp.json()
        self.token["expires_at"] = time.time() + self.token.get("expires_in", 3600) - 60
        TOKEN_PATH.write_text(json.dumps(self.token, indent=2))

    def _headers(self):
        self._refresh_if_needed()
        return {"Authorization": f"Bearer {self.token['access_token']}"}

    def _req(self, method, path, **kw):
        url = f"{API_BASE}{path}" if path.startswith("/") else path
        for attempt in range(4):
            resp = requests.request(method, url, headers=self._headers(), timeout=30, **kw)
            if resp.status_code == 429:
                time.sleep(2 ** attempt)
                continue
            if resp.status_code >= 400:
                raise RuntimeError(f"Pinterest API {resp.status_code}: {resp.text}")
            return resp.json()
        raise RuntimeError("Pinterest API rate-limited after 4 retries")

    def get_user(self) -> dict:
        return self._req("GET", "/user_account")

    def list_boards(self) -> list[dict]:
        items = []
        bookmark = None
        while True:
            params = {"page_size": 25}
            if bookmark:
                params["bookmark"] = bookmark
            data = self._req("GET", "/boards", params=params)
            items.extend(data.get("items", []))
            bookmark = data.get("bookmark")
            if not bookmark:
                break
        return items

    def create_pin(self, board_id: str, title: str, description: str,
                   link: str, image_path: str | Path) -> dict:
        image_path = Path(image_path)
        b64 = base64.b64encode(image_path.read_bytes()).decode()
        suffix = image_path.suffix.lower()
        content_type = "image/png" if suffix == ".png" else "image/jpeg"
        return self._req("POST", "/pins", json={
            "board_id": board_id,
            "title": title,
            "description": description,
            "link": link,
            "media_source": {
                "source_type": "image_base64",
                "content_type": content_type,
                "data": b64,
            },
        })

    def get_pin(self, pin_id: str) -> dict:
        return self._req("GET", f"/pins/{pin_id}")

    def delete_pin(self, pin_id: str):
        url = f"{API_BASE}/pins/{pin_id}"
        self._refresh_if_needed()
        resp = requests.delete(url, headers=self._headers(), timeout=30)
        if resp.status_code >= 400:
            raise RuntimeError(f"Pinterest API {resp.status_code}: {resp.text}")
