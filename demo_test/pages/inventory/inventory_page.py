class InventoryPage:

    def __init__(self, page):
        self.page = page

    # locators
    ADD_BACKPACK = "#add-to-cart-sauce-labs-backpack"
    CART_ICON = ".shopping_cart_link"
    TITLE = ".title"

    # actions
    def add_backpack_to_cart(self):
        self.page.click(self.ADD_BACKPACK)

    def go_to_cart(self):
        self.page.click(self.CART_ICON)

    # assertions helper
    def get_title(self):
        return self.page.text_content(self.TITLE)