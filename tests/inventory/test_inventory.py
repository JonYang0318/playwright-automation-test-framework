from pages.auth.login_page import LoginPage
from pages.inventory.inventory_page import InventoryPage

def test_login_and_add_cart(page):

    login = LoginPage(page)
    inventory = InventoryPage(page)

    # login
    login.open()
    login.login("standard_user", "secret_sauce")

    # inventory
    assert "inventory" in page.url

    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    assert "cart" in page.url