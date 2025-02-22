from utills.basepage import BasePage
import allure


class LoginPage(BasePage):
    """Page Object Model for Login Page."""

    def __init__(self, page):
        super().__init__(page)
        self.locators = {
            "username": "#j_username",
            "password": "#j_password",
            "login_button": "button[name='Submit']",
            "dashboard": "//a[normalize-space()='Dashboard']",
            "error_message": ".error-message"
        }

    @allure.step("Navigating to login page")
    def navigate_to(self, url: str) -> None:
        self.navigate(url)

    @allure.step("Entering username")
    def enter_username(self, username: str) -> None:
        self.fill(self.locators["username"], username)

    @allure.step("Entering password")
    def enter_password(self, password: str) -> None:
        self.fill(self.locators["password"], password)

    @allure.step("Clicking login button")
    def click_login(self) -> None:
        self.click(self.locators["login_button"])

    @allure.step("Verifying successful login")
    def verify_success(self) -> bool:
        return self.is_element_visible(self.locators["dashboard"])

    @allure.step("Verifying login failure")
    def verify_failure(self) -> bool:
        return self.is_element_visible(self.locators["error_message"])
