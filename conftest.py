import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from utils.config import VALID_PASSWORD, VALID_USER

@pytest.fixture
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=100
        )

        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()


@pytest.fixture
def logged_in_page(page):

    login = LoginPage(page)
    login.navigate()
    login.login(VALID_USER, VALID_PASSWORD)

    return page
