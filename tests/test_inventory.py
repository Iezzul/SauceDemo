from pages.inventory_page import InventoryPage
from playwright.sync_api import expect
from utils.config import INVENTORY_URL, PRODUCT_NAMES


def test_tc_011_inventory_page_loads(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    expect(logged_in_page).to_have_url(INVENTORY_URL)
    assert inventory.get_title_text() == "Products"


def test_tc_012_product_images_display(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    assert inventory.get_product_image_count() == 6
    assert inventory.are_all_product_images_visible() is True


def test_tc_013_product_names_display(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    assert inventory.get_product_names() == PRODUCT_NAMES


def test_tc_014_product_prices_display(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    assert len(inventory.get_product_prices()) == 6


def test_tc_015_sort_products_a_to_z(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.sort_products("az")

    assert inventory.get_product_names() == sorted(PRODUCT_NAMES)


def test_tc_016_sort_products_z_to_a(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.sort_products("za")

    assert inventory.get_product_names() == sorted(PRODUCT_NAMES, reverse=True)


def test_tc_017_sort_products_low_to_high(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.sort_products("lohi")

    prices = inventory.get_product_prices()
    assert prices == sorted(prices)


def test_tc_018_sort_products_high_to_low(logged_in_page):

    inventory = InventoryPage(logged_in_page)

    inventory.sort_products("hilo")

    prices = inventory.get_product_prices()
    assert prices == sorted(prices, reverse=True)
