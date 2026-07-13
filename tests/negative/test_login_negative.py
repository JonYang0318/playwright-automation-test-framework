from pages.auth.login_page import LoginPage


def test_login_wrong_password(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "standard_user",
        "wrong_password"
    )


    error = login.get_error_message()


    assert (
        "Username and password do not match"
        in error
    )


def test_login_empty_password(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "standard_user",
        ""
    )


    assert (
        "Password is required"
        in login.get_error_message()
    )

def test_locked_user_login(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "locked_out_user",
        "secret_sauce"
    )


    assert (
        "locked out"
        in login.get_error_message()
    )