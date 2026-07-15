# from pages.auth.login_page import LoginPage
# from pages.inventory.inventory_page import InventoryPage
# from pages.cart.cart_page import CartPage
# import allure
# import pytest

# @pytest.mark.smoke
# @allure.title("Add cart")
# def test_add_product_to_cart(page):

#     login = LoginPage(page)
#     inventory = InventoryPage(page)
#     cart = CartPage(page)


#     login.open()
#     login.login(
#         "standard_user",
#         "secret_sauce"
#     )

#     with allure.step("add product"):
#      inventory.add_backpack_to_cart()

#     with allure.step("go to cart"):
#      inventory.go_to_cart()

#     with allure.step("vertify"):
#      assert cart.get_cart_count() == 1