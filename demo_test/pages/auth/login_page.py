class LoginPage:

    def __init__(self, page):
        self.page = page


    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"

    ERROR_MESSAGE = "[data-test='error']"


    def open(self):
        self.page.goto(
            "https://www.saucedemo.com/"
        )


    def login(self, username, password):

        self.page.fill(
            self.USERNAME_INPUT,
            username
        )

        self.page.fill(
            self.PASSWORD_INPUT,
            password
        )

        self.page.click(
            self.LOGIN_BUTTON
        )


    def get_error_message(self):

        return self.page.locator(
            self.ERROR_MESSAGE
        ).text_content()