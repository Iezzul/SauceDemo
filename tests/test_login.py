from pages.login_page import LoginPage
from playwright.sync_api import expect
from utils.config import (
    BASE_URL,
    INVALID_CREDENTIALS_ERROR,
    INVALID_PASSWORD,
    INVALID_USER,
    LOCKED_OUT_ERROR,
    LOCKED_OUT_USER,
    PASSWORD_REQUIRED_ERROR,
    USERNAME_REQUIRED_ERROR,
    VALID_PASSWORD,
    VALID_USER,
)

def test_tc_001_valid_login(page):

    login = LoginPage(page)

    login.navigate()
    login.login(
        VALID_USER,
        VALID_PASSWORD
    )

    expect(page).to_have_url(
        f"{BASE_URL}inventory.html"
    )


def test_tc_002_invalid_username_shows_error(page):

    login = LoginPage(page)

    login.navigate()
    login.login(
        INVALID_USER,
        VALID_PASSWORD
    )

    expect(page).to_have_url(BASE_URL)
    assert login.get_error_message() == INVALID_CREDENTIALS_ERROR


def test_tc_003_invalid_password_shows_error(page):

    login = LoginPage(page)

    login.navigate()
    login.login(
        VALID_USER,
        INVALID_PASSWORD
    )

    expect(page).to_have_url(BASE_URL)
    assert login.get_error_message() == INVALID_CREDENTIALS_ERROR


def test_tc_004_empty_username_shows_error(page):

    login = LoginPage(page)

    login.navigate()
    login.login(
        "",
        VALID_PASSWORD
    )

    expect(page).to_have_url(BASE_URL)
    assert login.get_error_message() == USERNAME_REQUIRED_ERROR


def test_tc_005_empty_password_shows_error(page):

    login = LoginPage(page)

    login.navigate()
    login.login(
        VALID_USER,
        ""
    )

    expect(page).to_have_url(BASE_URL)
    assert login.get_error_message() == PASSWORD_REQUIRED_ERROR


def test_tc_006_empty_credentials_shows_error(page):

    login = LoginPage(page)

    login.navigate()
    login.click_login()

    expect(page).to_have_url(BASE_URL)
    assert login.get_error_message() == USERNAME_REQUIRED_ERROR


def test_tc_007_locked_out_user_shows_error(page):

    login = LoginPage(page)

    login.navigate()
    login.login(
        LOCKED_OUT_USER,
        VALID_PASSWORD
    )

    expect(page).to_have_url(BASE_URL)
    assert login.get_error_message() == LOCKED_OUT_ERROR


def test_tc_008_password_field_is_masked(page):

    login = LoginPage(page)

    login.navigate()

    assert login.get_password_input_type() == "password"


def test_tc_009_login_with_enter_key(page):

    login = LoginPage(page)

    login.navigate()
    login.press_enter_to_login(
        VALID_USER,
        VALID_PASSWORD
    )

    expect(page).to_have_url(
        f"{BASE_URL}inventory.html"
    )
