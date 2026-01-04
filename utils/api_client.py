import json
import uuid
import requests
from typing import Any, Dict, Optional

from utils.config import (
    BASE_URL,
    PUBLIC_API_KEY,
    PRIVATE_SECRET_KEY,
    ACCOUNT_ID,
    validate_config,
)

class ApiClient:
    def __init__(self) -> None:
        validate_config()
        self.base_url = BASE_URL.rstrip("/")
        self.session = requests.Session()

    def _headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        headers = {
            "Content-Type": "application/json",
            # Common auth style - adjust if API expects different header names
            "public-api-key": PUBLIC_API_KEY,
            "private-secret-key": PRIVATE_SECRET_KEY,
            "x-idempotency-key": str(uuid.uuid4()),
        }
        if extra:
            headers.update(extra)
        return headers

    def request(
        self,
        method: str,
        path: str,
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 30,
    ) -> requests.Response:
        url = f"{self.base_url}{path}"
        body = None if payload is None else json.dumps(payload)

        resp = self.session.request(
            method=method.upper(),
            url=url,
            data=body,
            headers=self._headers(headers),
            timeout=timeout,
        )
        return resp

    # Convenience methods
    def post(self, path: str, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None) -> requests.Response:
        return self.request("POST", path, payload=payload, headers=headers)

    def get(self, path: str, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        return self.request("GET", path, payload=None, headers=headers)

    def put(self, path: str, payload: Dict[str, Any], headers: Optional[Dict[str, str]] = None) -> requests.Response:
        return self.request("PUT", path, payload=payload, headers=headers)

    def delete(self, path: str, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        return self.request("DELETE", path, payload=None, headers=headers)
