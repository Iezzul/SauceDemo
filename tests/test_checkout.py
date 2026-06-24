from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect
from utils.config import (
    CART_URL,
    CHECKOUT_COMPLETE_URL,
    CHECKOUT_STEP_ONE_URL,
    CHECKOUT_STEP_TWO_URL,
    FIRST_NAME_REQUIRED_ERROR,
    LAST_NAME_REQUIRED_ERROR,
    POSTAL_CODE_REQUIRED_ERROR,
    PRODUCT_NAMES,
    USER_DETAILS,
)

def test_tc_026_proceed_to_checkout(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()

    cart.checkout()

    expect(logged_in_page).to_have_url(CHECKOUT_STEP_ONE_URL)
    assert checkout.get_title_text() == "Checkout: Your Information"


def test_tc_027_submit_valid_checkout_details(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()

    cart.checkout()
    checkout.enter_information(
        USER_DETAILS["first_name"],
        USER_DETAILS["last_name"],
        USER_DETAILS["postal_code"]
    )

    expect(logged_in_page).to_have_url(CHECKOUT_STEP_TWO_URL)
    assert checkout.get_title_text() == "Checkout: Overview"


def test_tc_028_checkout_without_first_name(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()
    cart.checkout()
    checkout.enter_information(
        "",
        USER_DETAILS["last_name"],
        USER_DETAILS["postal_code"]
    )

    assert checkout.get_error_message() == FIRST_NAME_REQUIRED_ERROR


def test_tc_029_checkout_without_last_name(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()
    cart.checkout()
    checkout.enter_information(
        USER_DETAILS["first_name"],
        "",
        USER_DETAILS["postal_code"]
    )

    assert checkout.get_error_message() == LAST_NAME_REQUIRED_ERROR


def test_tc_030_checkout_without_postal_code(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()
    cart.checkout()
    checkout.enter_information(
        USER_DETAILS["first_name"],
        USER_DETAILS["last_name"],
        ""
    )

    assert checkout.get_error_message() == POSTAL_CODE_REQUIRED_ERROR


def test_tc_031_verify_checkout_overview(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()
    cart.checkout()
    checkout.enter_information(
        USER_DETAILS["first_name"],
        USER_DETAILS["last_name"],
        USER_DETAILS["postal_code"]
    )

    expect(logged_in_page).to_have_url(CHECKOUT_STEP_TWO_URL)
    assert checkout.get_title_text() == "Checkout: Overview"


def test_tc_032_verify_product_details_in_overview(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()
    cart.checkout()
    checkout.enter_information(
        USER_DETAILS["first_name"],
        USER_DETAILS["last_name"],
        USER_DETAILS["postal_code"]
    )

    assert checkout.get_overview_item_names() == [PRODUCT_NAMES[0]]
    assert checkout.get_overview_item_prices() == ["$29.99"]


def test_tc_033_verify_tax_information(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()
    cart.checkout()
    checkout.enter_information(
        USER_DETAILS["first_name"],
        USER_DETAILS["last_name"],
        USER_DETAILS["postal_code"]
    )

    assert "Tax:" in checkout.get_tax_text()


def test_tc_034_complete_purchase(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()
    cart.checkout()
    checkout.enter_information(
        USER_DETAILS["first_name"],
        USER_DETAILS["last_name"],
        USER_DETAILS["postal_code"]
    )
    checkout.finish_order()

    expect(logged_in_page).to_have_url(CHECKOUT_COMPLETE_URL)
    assert checkout.get_success_message() == "Thank you for your order!"


def test_tc_035_cancel_checkout(logged_in_page):

    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_backpack()
    inventory.open_cart()
    cart.checkout()
    checkout.cancel()

    expect(logged_in_page).to_have_url(CART_URL)
