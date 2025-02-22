import pytest
from pageobject.loginpage import LoginPage
import allure


@allure.feature("Authentication")
@allure.story("User Login")
@pytest.mark.parametrize("scenario", ["valid", "invalid", "empty"])
def test_login_scenarios(page, config, scenario):
    """Test login functionality with different credential scenarios."""
    login_page = LoginPage(page)
    creds = config['credentials'][scenario]

    with allure.step(f"Testing login with {scenario} credentials"):
        login_page.navigate_to(config['urls']['login_url'])
        login_page.enter_username(creds['username'])
        login_page.enter_password(creds['password'])
        login_page.click_login()

        if scenario == "valid":
            assert login_page.verify_success(), "Login should succeed with valid credentials"
        else:
            assert login_page.verify_failure(), f"Login should fail with {scenario} credentials"