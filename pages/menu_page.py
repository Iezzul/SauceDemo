class MenuPage:

    def __init__(self, page):
        self.page = page
        self.menu_panel = ".bm-menu-wrap"

    def open_menu(self):
        self.page.click("#react-burger-menu-btn")
        self.page.wait_for_timeout(600)

    def close_menu(self):
        self.page.click("#react-burger-cross-btn")
        self.page.wait_for_timeout(600)

    def logout(self):
        self.page.click("#logout_sidebar_link")

    def reset_app_state(self):
        self.page.click("#reset_sidebar_link")

    def is_menu_visible(self):
        box = self.page.locator(self.menu_panel).bounding_box()
        return box is not None and box["x"] > -1
