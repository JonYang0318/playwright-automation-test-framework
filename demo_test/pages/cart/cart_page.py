class CartPage:

    def __init__(self, page):
        self.page = page

    CHECKOUT_BUTTON = "#checkout"

    def click_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)

    def get_cart_count(self):
        return self.page.locator(self.CART_ITEMS).count()

    def has_product(self, product_name):
        return self.page.locator(
            f".inventory_item_name:text-is('{product_name}')"
        ).is_visible()

    def get_product_price(self, product_name):

        item = self.page.locator(
            ".cart_item"
        ).filter(
            has_text=product_name
        )

        return item.locator(
            ".inventory_item_price"
        ).text_content()

    def is_checkout_button_visible(self):
        return self.page.locator(
            self.CHECKOUT_BUTTON
        ).is_visible()