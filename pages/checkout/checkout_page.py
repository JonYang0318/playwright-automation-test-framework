class CheckoutPage:

    def __init__(self, page):
        self.page = page
    
    CHECKOUT_BUTTON = "#checkout"

    def click_checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)


    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"

    CONTINUE_BUTTON = "#continue"

    ERROR_MESSAGE = "[data-test='error']"

    def fill_checkout_info(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.page.fill(
            self.FIRST_NAME,
            first_name
        )

        self.page.fill(
            self.LAST_NAME,
            last_name
        )

        self.page.fill(
            self.POSTAL_CODE,
            postal_code
        )

    def click_continue(self):
        self.page.click(
            self.CONTINUE_BUTTON
        )

    def get_error_message(self):

        return self.page.locator(
            self.ERROR_MESSAGE
        ).text_content()
    
 
