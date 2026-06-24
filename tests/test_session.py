from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from playwright.sync_api import expect
from utils.config import BASE_URL, INVENTORY_URL, VALID_PASSWORD, VALID_USER


def test_tc_039_access_inventory_after_logout(page):

    login = LoginPage(page)
    menu = MenuPage(page)

    login.navigate()
    login.login(VALID_USER, VALID_PASSWORD)
    menu.open_menu()
    menu.logout()

    page.goto(INVENTORY_URL)

    expect(page).to_have_url(BASE_URL)


def test_tc_040_browser_back_after_logout(page):

    login = LoginPage(page)
    menu = MenuPage(page)

    login.navigate()
    login.login(VALID_USER, VALID_PASSWORD)
    menu.open_menu()
    menu.logout()

    page.go_back()

    expect(page).to_have_url(BASE_URL)
