class InventoryPage:

    def __init__(self, page):
        self.page = page

    cart_icon = '[data-test="shopping-cart-link"]'
    cart_badge = '[data-test="shopping-cart-badge"]'
    title = '[data-test="title"]'
    item_name = '[data-test="inventory-item-name"]'
    item_price = '[data-test="inventory-item-price"]'
    item_image = '.inventory_item_img img'
    sort_dropdown = '[data-test="product-sort-container"]'

    def add_backpack(self):
        self.page.click('[data-test="add-to-cart-sauce-labs-backpack"]')

    def add_bike_light(self):
        self.page.click('[data-test="add-to-cart-sauce-labs-bike-light"]')

    def remove_backpack(self):
        self.page.click('[data-test="remove-sauce-labs-backpack"]')

    def add_all_products(self):
        self.page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.page.click('[data-test="add-to-cart-sauce-labs-bike-light"]')
        self.page.click('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
        self.page.click('[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
        self.page.click('[data-test="add-to-cart-sauce-labs-onesie"]')
        self.page.click('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')

    def open_cart(self):
        self.page.click(self.cart_icon)

    def get_cart_badge_count(self):
        return self.page.locator(self.cart_badge).text_content()

    def get_title_text(self):
        return self.page.locator(self.title).text_content()

    def get_product_names(self):
        return self.page.locator(self.item_name).all_text_contents()

    def get_product_prices(self):
        prices = self.page.locator(self.item_price).all_text_contents()
        return [float(price.replace("$", "")) for price in prices]

    def get_product_image_count(self):
        return self.page.locator(self.item_image).count()

    def are_all_product_images_visible(self):
        images = self.page.locator(self.item_image)
        return all(images.nth(index).is_visible() for index in range(images.count()))

    def sort_products(self, sort_value):
        self.page.select_option(self.sort_dropdown, sort_value)

    def is_cart_badge_visible(self):
        return self.page.locator(self.cart_badge).is_visible()
