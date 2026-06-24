# SauceDemo Playwright Automation

This project is my practice automation framework for the SauceDemo website using Python, Playwright, and Pytest.

I created it to learn how a real test automation project is structured, not just how to record steps and replay them. I used Page Object Model so the tests are cleaner, easier to read, and easier to maintain.

The test coverage in this project includes `TC_001` until `TC_040`.

## About This Project

I am a fresh graduate and I built this project as part of my QA automation learning journey.

With this project, I wanted to practice:

- writing UI automation tests
- organizing tests by feature
- using Page Object Model
- keeping reusable data in config files
- running tests with Pytest

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model

## Project Structure

```text
SauceDemo/
|-- conftest.py
|-- README.md
|-- learnme.md
|-- utils/
|   `-- config.py
|-- pages/
|   |-- login_page.py
|   |-- inventory_page.py
|   |-- cart_page.py
|   |-- checkout_page.py
|   `-- menu_page.py
`-- tests/
    |-- test_login.py
    |-- test_logout.py
    |-- test_inventory.py
    |-- test_cart.py
    |-- test_checkout.py
    |-- test_menu.py
    `-- test_session.py
```

## How The Framework Is Organized

This project uses Page Object Model.

- `tests/` contains the test cases
- `pages/` contains locators and page actions
- `utils/config.py` stores reusable test data
- `conftest.py` stores shared fixtures

This helps keep the test files shorter and easier to understand.

## Test Coverage

- `TC_001 - TC_009` Login
- `TC_010` Logout
- `TC_011 - TC_018` Inventory
- `TC_019 - TC_025` Cart
- `TC_026 - TC_035` Checkout
- `TC_036 - TC_038` Menu
- `TC_039 - TC_040` Session Security

## What Is Automated

- valid and invalid login
- locked out user validation
- password masking
- login using Enter key
- product name, image, and price checks
- product sorting
- add to cart and remove from cart
- continue shopping flow
- checkout validation
- complete purchase flow
- side menu actions
- reset app state
- logout
- session protection after logout

## Learning Notes

I also wrote `learnme.md` for myself as a beginner note.

It contains:

- explanation of the framework structure
- where the main code is
- common testing shortforms
- useful pytest commands

## Sample Result

Full suite command:

```powershell
python -m pytest tests -q
```

Example result:

```text
40 passed
```

## Why I Made This

I wanted a project that shows more than just a recorded automation script.

This project helped me practice writing proper test files, reusing page objects, and understanding how a small automation framework works from end to end.

I am still learning, and I am interested to keep exploring more in QA automation.
