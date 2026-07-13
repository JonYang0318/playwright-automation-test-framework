from pages.auth.login_page import LoginPage
from pages.inventory.inventory_page import InventoryPage
from pages.cart.cart_page import CartPage
from pages.checkout.checkout_page import CheckoutPage


def test_checkout_success(page):

    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

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

    assert "checkout-step-two" in page.url