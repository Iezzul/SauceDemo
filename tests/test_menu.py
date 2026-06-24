from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.menu_page import MenuPage
from playwright.sync_api import expect
from utils.config import CART_URL


def test_tc_036_open_side_menu(logged_in_page):

    menu = MenuPage(logged_in_page)

    menu.open_menu()

    assert menu.is_menu_visible() is True


def test_tc_037_close_side_menu(logged_in_page):

    menu = MenuPage(logged_in_page)

    menu.open_menu()
    menu.close_menu()

    assert menu.is_menu_visible() is False


def test_tc_038_reset_app_state(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    menu = MenuPage(logged_in_page)
    cart = CartPage(logged_in_page)

    inventory.add_backpack()
    assert inventory.get_cart_badge_count() == "1"

    menu.open_menu()
    menu.reset_app_state()
    menu.close_menu()

    assert inventory.is_cart_badge_visible() is False

    inventory.open_cart()
    expect(logged_in_page).to_have_url(CART_URL)
    assert cart.get_cart_items_count() == 0
