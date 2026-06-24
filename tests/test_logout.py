from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from playwright.sync_api import expect
from utils.config import BASE_URL

def test_tc_010_logout(page):

    login = LoginPage(page)
    menu = MenuPage(page)

    login.navigate()
    login.login(
        "standard_user",
        "secret_sauce"
    )

    menu.open_menu()
    menu.logout()

    expect(page).to_have_url(
        BASE_URL
    )
