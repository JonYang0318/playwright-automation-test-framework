class FinishPage:

    def __init__(self, page):
        self.page = page

    FINISH_BUTTON = "#finish"
    COMPLETE_HEADER = ".complete-header"

    def click_finish(self):
        self.page.click(self.FINISH_BUTTON)

    def get_complete_message(self):
        return self.page.locator(
            self.COMPLETE_HEADER
        ).text_content()