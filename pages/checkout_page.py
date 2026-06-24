class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self.error_message = '[data-test="error"]'
        self.tax_label = '.summary_tax_label'
        self.title = '[data-test="title"]'
        self.item_name = '[data-test="inventory-item-name"]'
        self.item_price = '[data-test="inventory-item-price"]'

    def enter_information(self, first, last, postal):
        self.page.fill('[data-test="firstName"]', first)
        self.page.fill('[data-test="lastName"]', last)
        self.page.fill('[data-test="postalCode"]', postal)

        self.page.click('[data-test="continue"]')

    def finish_order(self):
        self.page.click('[data-test="finish"]')

    def get_success_message(self):
        return self.page.locator(".complete-header").text_content()

    def cancel(self):
        self.page.click('[data-test="cancel"]')

    def get_error_message(self):
        return self.page.locator(self.error_message).text_content()

    def get_title_text(self):
        return self.page.locator(self.title).text_content()

    def get_overview_item_names(self):
        return self.page.locator(self.item_name).all_text_contents()

    def get_overview_item_prices(self):
        return self.page.locator(self.item_price).all_text_contents()

    def get_tax_text(self):
        return self.page.locator(self.tax_label).text_content()
