"""Thin Etsy Open API v3 client: auth refresh + listing/image/file wrappers.

Used by publish_all.py. Requires token.json (run auth.py first) and a filled
.env. Endpoints verified against Etsy Open API v3 reference; a few values
(shop_id, taxonomy_id) are resolved at runtime and logged.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import requests

from auth import ENV_PATH, TOKEN_PATH, TOKEN_URL, load_env  # reuse

API = "https://openapi.etsy.com/v3/application"


class EtsyClient:
    def __init__(self):
        self.env = load_env()
        self.keystring = self.env["ETSY_KEYSTRING"]
        self.shared_secret = self.env["ETSY_SHARED_SECRET"]
        self.token = self._load_token()

    # ---- auth ----
    def _load_token(self) -> dict:
        if not TOKEN_PATH.exists():
            raise SystemExit("No token.json — run auth.py first to authorize.")
        return json.loads(TOKEN_PATH.read_text())

    def _save_token(self):
        TOKEN_PATH.write_text(json.dumps(self.token, indent=2))

    def _refresh_if_needed(self):
        if time.time() < self.token.get("expires_at", 0):
            return
        resp = requests.post(TOKEN_URL, data={
            "grant_type": "refresh_token",
            "client_id": self.keystring,
            "refresh_token": self.token["refresh_token"],
        }, timeout=30)
        resp.raise_for_status()
        new = resp.json()
        self.token.update(new)
        self.token["expires_at"] = time.time() + new.get("expires_in", 3600) - 60
        self._save_token()

    def _headers(self, json_ct=False) -> dict:
        self._refresh_if_needed()
        # Etsy expects x-api-key as "keystring:shared_secret" for this app
        h = {"x-api-key": f"{self.keystring}:{self.shared_secret}",
             "Authorization": f"Bearer {self.token['access_token']}"}
        if json_ct:
            h["Content-Type"] = "application/json"
        return h

    # ---- core request with basic 429 retry ----
    def _req(self, method: str, path: str, **kw):
        url = path if path.startswith("http") else f"{API}{path}"
        for attempt in range(4):
            files = kw.get("files")
            headers = self._headers()
            if files is None and kw.get("data") is None and method in ("POST", "PATCH", "PUT"):
                pass
            resp = requests.request(method, url, headers=headers, timeout=60, **kw)
            if resp.status_code == 429:
                time.sleep(2 ** attempt)
                continue
            if resp.status_code >= 400:
                raise RuntimeError(f"{method} {url} -> {resp.status_code}: {resp.text}")
            return resp.json() if resp.text else {}
        raise RuntimeError(f"{method} {url} rate-limited after retries")

    # ---- identity / shop ----
    def get_me(self) -> dict:
        # access_token is "<user_id>.<rand>"; /users/me returns user_id + shop_id
        return self._req("GET", "/users/me")

    def get_shop_id(self) -> int:
        if self.env.get("ETSY_SHOP_ID"):
            return int(self.env["ETSY_SHOP_ID"])
        # user_id is the prefix of the OAuth access token ("<uid>.<rand>")
        uid = self.token["access_token"].split(".")[0]
        shops = self._req("GET", f"/users/{uid}/shops")
        if isinstance(shops, dict) and shops.get("shop_id"):
            return int(shops["shop_id"])
        results = shops.get("results") if isinstance(shops, dict) else None
        if results:
            return int(results[0]["shop_id"])
        raise SystemExit("No Etsy shop found for this account — open an Etsy shop first.")

    # ---- taxonomy ----
    def find_taxonomy_id(self, name="Puzzles") -> int | None:
        nodes = self._req("GET", "/seller-taxonomy/nodes")
        target = name.lower()
        stack = list(nodes.get("results", []))
        while stack:
            n = stack.pop()
            if n.get("name", "").lower() == target:
                return n["id"]
            stack.extend(n.get("children") or [])
        return None

    # ---- listings ----
    def create_draft_listing(self, shop_id: int, *, title: str, description: str,
                             price: float, taxonomy_id: int, tags: list[str],
                             quantity: int = 999, who_made="i_did",
                             when_made="2020_2025") -> dict:
        data = {
            "quantity": quantity,
            "title": title[:140],
            "description": description,
            "price": price,
            "who_made": who_made,
            "when_made": when_made,
            "taxonomy_id": taxonomy_id,
            "type": "download",          # digital listing
            "should_auto_renew": "false",
            "state": "draft",
        }
        # tags: list -> repeated form fields handled by Etsy as comma list
        for i, t in enumerate(tags[:13]):
            data[f"tags[{i}]"] = t
        return self._req("POST", f"/shops/{shop_id}/listings", data=data)

    def update_listing_tags(self, shop_id: int, listing_id: int, tags: list[str]):
        return self._req("PATCH", f"/shops/{shop_id}/listings/{listing_id}",
                         data={"tags": ",".join(tags[:13])})

    def upload_image(self, shop_id: int, listing_id: int, path: str, rank: int = 1):
        with open(path, "rb") as f:
            files = {"image": (Path(path).name, f, "image/png")}
            return self._req("POST",
                             f"/shops/{shop_id}/listings/{listing_id}/images",
                             data={"rank": rank}, files=files)

    def upload_file(self, shop_id: int, listing_id: int, path: str, name: str | None = None):
        with open(path, "rb") as f:
            fname = name or Path(path).name
            files = {"file": (fname, f, "application/octet-stream")}
            return self._req("POST",
                             f"/shops/{shop_id}/listings/{listing_id}/files",
                             data={"name": fname}, files=files)


if __name__ == "__main__":
    c = EtsyClient()
    print("Shop ID:", c.get_shop_id())
    print("Puzzles taxonomy_id:", c.find_taxonomy_id("Puzzles"))
