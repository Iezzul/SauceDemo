from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import expect
from utils.config import CART_URL, INVENTORY_URL, PRODUCT_NAMES

def test_tc_019_add_item_to_cart(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.add_backpack()

    assert inventory.get_cart_badge_count() == "1"


def test_tc_020_add_multiple_items_to_cart(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.add_all_products()

    assert inventory.get_cart_badge_count() == "6"


def test_tc_021_remove_item_from_inventory_page(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.add_backpack()
    inventory.remove_backpack()

    assert inventory.is_cart_badge_visible() is False


def test_tc_022_open_shopping_cart(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)

    inventory.open_cart()

    expect(logged_in_page).to_have_url(CART_URL)
    assert cart.get_title_text() == "Your Cart"


def test_tc_023_verify_cart_item_details(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()

    assert cart.get_item_names() == [PRODUCT_NAMES[0]]
    assert cart.get_item_prices() == ["$29.99"]


def test_tc_024_remove_item_from_cart(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()
    cart.remove_backpack()

    assert cart.get_cart_items_count() == 0


def test_tc_025_continue_shopping(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)

    inventory.open_cart()
    cart.continue_shopping()

    expect(logged_in_page).to_have_url(INVENTORY_URL)
