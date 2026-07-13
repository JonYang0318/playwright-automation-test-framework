import pytest
import allure
def test_fail_screenshot(page):

    page.goto(
        "https://www.saucedemo.com/"
    )

    assert False