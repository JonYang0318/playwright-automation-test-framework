import pytest
import allure
from pages.auth.login_page import LoginPage
from utils.data_reader import load_login_data
login_data = load_login_data()




@pytest.mark.parametrize(
    "user_type",
    [
        "valid_user",
        "wrong_password",
        "locked_user"
    ]
)

@pytest.mark.smoke
@allure.title("Login test - {user_type}")
def test_login_data_driven(page, user_type):

    login = LoginPage(page)

    data = login_data[user_type]


    with allure.step("Open login page"):

        login.open()


    with allure.step("Enter username and password"):

        login.login(
            data["username"],
            data["password"]
        )


    if data["expected"] == "success":

        with allure.step("Verify login success"):

            assert "inventory" in page.url


    else:

        with allure.step("Verify error message"):

            error_message = login.get_error_message()

            assert data["expected"] in error_message


@pytest.mark.smoke
@allure.title("Login fail")
def test_login_fail(page):

    login = LoginPage(page)

    with allure.step("Open login page"):
        login.open()

    with allure.step("Enter username and password"):
        login.login(
      login_data["valid_user"]["username"],
      login_data["valid_user"]["password"]
        )
    
    error = page.locator(
        "[data-test='error']"
    )
    # assert False
    with allure.step("Verify login fail"):
      assert error.is_visible()