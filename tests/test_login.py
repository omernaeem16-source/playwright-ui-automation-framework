import os

import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username, password, expected",
    [
        # Valid credentials: login should succeed
        (os.getenv("QA_USERNAME"), os.getenv("QA_PASSWORD"), "success"),

        # Invalid username and password combinations: login should fail
        ("wrong_user", "wrong_pass", "failure"),
        ("omernaeem16@gmail.com", "wrong_pass", "failure"),
        ("wrong_user", "wrong_pass", "failure"),
    ],
)
def test_login(page, username, password, expected):
    # Ensure the valid-login scenario has credentials configured
    if expected == "success":
        assert username and password, (
            "Set QA_USERNAME and QA_PASSWORD in the project .env file."
        )

    # Open the login page and submit the selected credentials
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)

    # Verify the outcome for this set of credentials
    if expected == "success":
        expect(page).to_have_url("https://qademo.com/catalog")
    else:
        expect(login_page.error_message).to_have_text(
            "Invalid username or password"
        )

