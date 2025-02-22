from playwright.sync_api import Page, TimeoutError as PlaywrightTimeout
import logging
from typing import Optional, List
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = logging.getLogger(__name__)

    def navigate(self, url: str, timeout: int = 30000) -> None:
        """Navigate to URL with timeout."""
        with allure.step(f"Navigating to {url}"):
            try:
                self.page.goto(url, timeout=timeout)
                self.logger.info(f"Successfully navigated to {url}")
            except PlaywrightTimeout:
                self.logger.error(f"Navigation timeout to {url}")
                raise
            except Exception as e:
                self.logger.error(f"Navigation failed: {e}")
                raise

    def click(self, selector: str, timeout: int = 10000) -> None:
        """Click element with retry mechanism."""
        with allure.step(f"Clicking element: {selector}"):
            try:
                self.page.wait_for_selector(selector, state="visible", timeout=timeout)
                self.page.click(selector)
                self.logger.info(f"Clicked {selector}")
            except Exception as e:
                self.logger.error(f"Click failed on {selector}: {e}")
                raise

    def fill(self, selector: str, value: str, timeout: int = 10000) -> None:
        """Fill input field."""
        with allure.step(f"Filling {selector} with '{value}'"):
            try:
                self.page.wait_for_selector(selector, state="visible", timeout=timeout)
                self.page.fill(selector, value)
                self.logger.info(f"Filled {selector} with {value}")
            except Exception as e:
                self.logger.error(f"Fill failed on {selector}: {e}")
                raise

    def get_text(self, selector: str, timeout: int = 10000) -> Optional[str]:
        """Retrieve element text."""
        with allure.step(f"Getting text from {selector}"):
            try:
                self.page.wait_for_selector(selector, state="visible", timeout=timeout)
                text = self.page.text_content(selector)
                self.logger.info(f"Text retrieved from {selector}: {text}")
                return text
            except Exception as e:
                self.logger.error(f"Failed to get text from {selector}: {e}")
                raise

    def is_element_visible(self, selector: str, timeout: int = 10000) -> bool:
        """Check if element is visible."""
        with allure.step(f"Checking visibility of {selector}"):
            try:
                return self.page.is_visible(selector, timeout=timeout)
            except Exception as e:
                self.logger.error(f"Visibility check failed for {selector}: {e}")
                raise
