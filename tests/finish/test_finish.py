from pages.auth.login_page import LoginPage
from pages.inventory.inventory_page import InventoryPage
from pages.cart.cart_page import CartPage
from pages.checkout.checkout_page import CheckoutPage
from pages.finish.finish_page import FinishPage


def test_order_complete(page):

    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)
    finish = FinishPage(page)


    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )


    inventory.add_backpack_to_cart()

    inventory.go_to_cart()


    cart.click_checkout()


    checkout.fill_checkout_info(
        "John",
        "Doe",
        "100"
    )

    checkout.click_continue()


    finish.click_finish()


    assert finish.get_complete_message() == \
        "Thank you for your order!"