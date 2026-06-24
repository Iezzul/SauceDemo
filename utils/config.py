# config.py
BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = f"{BASE_URL}inventory.html"
CART_URL = f"{BASE_URL}cart.html"
CHECKOUT_STEP_ONE_URL = f"{BASE_URL}checkout-step-one.html"
CHECKOUT_STEP_TWO_URL = f"{BASE_URL}checkout-step-two.html"
CHECKOUT_COMPLETE_URL = f"{BASE_URL}checkout-complete.html"

# Credentials
VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"
LOCKED_OUT_USER = "locked_out_user"

INVALID_USER = "wrong_user"
INVALID_PASSWORD = "secret_sauce123"

# Login Error Messages
INVALID_CREDENTIALS_ERROR = (
    "Epic sadface: Username and password do not match any user in this service"
)
LOCKED_OUT_ERROR = (
    "Epic sadface: Sorry, this user has been locked out."
)
USERNAME_REQUIRED_ERROR = "Epic sadface: Username is required"
PASSWORD_REQUIRED_ERROR = "Epic sadface: Password is required"
FIRST_NAME_REQUIRED_ERROR = "Error: First Name is required"
LAST_NAME_REQUIRED_ERROR = "Error: Last Name is required"
POSTAL_CODE_REQUIRED_ERROR = "Error: Postal Code is required"

PRODUCT_NAMES = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)",
]

# Checkout Information
USER_DETAILS = {
    "first_name": "Amri",
    "last_name": "Rizqi",
    "postal_code": "54400"
}
