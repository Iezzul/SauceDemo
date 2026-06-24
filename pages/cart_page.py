class CartPage:

    def __init__(self, page):
        self.page = page
        self.title = '[data-test="title"]'
        self.item_name = '[data-test="inventory-item-name"]'
        self.item_price = '[data-test="inventory-item-price"]'
        self.continue_shopping_button = '[data-test="continue-shopping"]'

    def remove_backpack(self):
        self.page.click('[data-test="remove-sauce-labs-backpack"]')

    def remove_bike_light(self):
        self.page.click('[data-test="remove-sauce-labs-bike-light"]')

    def checkout(self):
        self.page.click('[data-test="checkout"]')

    def get_cart_items_count(self):
        return self.page.locator('[data-test="inventory-item"]').count()

    def get_title_text(self):
        return self.page.locator(self.title).text_content()

    def get_item_names(self):
        return self.page.locator(self.item_name).all_text_contents()

    def get_item_prices(self):
        return self.page.locator(self.item_price).all_text_contents()

    def continue_shopping(self):
        self.page.click(self.continue_shopping_button)
