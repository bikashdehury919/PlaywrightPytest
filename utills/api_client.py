# utils/api_client.py
import allure
import logging
from typing import Dict, Any, Optional
from playwright.sync_api import APIRequestContext
import requests


class APIClient:
    def __init__(self, request_context: Optional[APIRequestContext] = None,
                 http_session: Optional[requests.Session] = None, base_url: str = ""):
        self.request_context = request_context
        self.http_session = http_session
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    @allure.step("Sending GET request to {endpoint}")
    def get(self, endpoint: str, params: Dict[str, Any] = None) -> Dict:
        """Send a GET request."""
        try:
            if self.request_context:
                response = self.request_context.get(endpoint, params=params)
                status = response.status
                body = response.json()
            elif self.http_session:
                response = self.http_session.get(f"{self.base_url}{endpoint}", params=params)
                status = response.status_code
                body = response.json()
            else:
                raise ValueError("No request context or session provided")

            self.logger.info(f"GET {endpoint} - Status: {status}")
            allure.attach(str(body), name="Response", attachment_type=allure.attachment_type.JSON)
            return {"status": status, "body": body}
        except Exception as e:
            self.logger.error(f"GET {endpoint} failed: {e}")
            raise

    @allure.step("Sending POST request to {endpoint}")
    def post(self, endpoint: str, data: Dict[str, Any] = None) -> Dict:
        """Send a POST request."""
        try:
            if self.request_context:
                response = self.request_context.post(endpoint, data=data)
                status = response.status
                body = response.json()
            elif self.http_session:
                response = self.http_session.post(f"{self.base_url}{endpoint}", json=data)
                status = response.status_code
                body = response.json()

            self.logger.info(f"POST {endpoint} - Status: {status}")
            allure.attach(str(body), name="Response", attachment_type=allure.attachment_type.JSON)
            return {"status": status, "body": body}
        except Exception as e:
            self.logger.error(f"POST {endpoint} failed: {e}")
            raise

    @allure.step("Sending PUT request to {endpoint}")
    def put(self, endpoint: str, data: Dict[str, Any] = None) -> Dict:
        """Send a PUT request."""
        try:
            if self.request_context:
                response = self.request_context.put(endpoint, data=data)
                status = response.status
                body = response.json()
            elif self.http_session:
                response = self.http_session.put(f"{self.base_url}{endpoint}", json=data)
                status = response.status_code
                body = response.json()

            self.logger.info(f"PUT {endpoint} - Status: {status}")
            allure.attach(str(body), name="Response", attachment_type=allure.attachment_type.JSON)
            return {"status": status, "body": body}
        except Exception as e:
            self.logger.error(f"PUT {endpoint} failed: {e}")
            raise

    @allure.step("Sending DELETE request to {endpoint}")
    def delete(self, endpoint: str) -> Dict:
        """Send a DELETE request."""
        try:
            if self.request_context:
                response = self.request_context.delete(endpoint)
                status = response.status
                body = response.json() if response.body() else {}
            elif self.http_session:
                response = self.http_session.delete(f"{self.base_url}{endpoint}")
                status = response.status_code
                body = response.json() if response.content else {}

            self.logger.info(f"DELETE {endpoint} - Status: {status}")
            allure.attach(str(body), name="Response", attachment_type=allure.attachment_type.JSON)
            return {"status": status, "body": body}
        except Exception as e:
            self.logger.error(f"DELETE {endpoint} failed: {e}")
            raise