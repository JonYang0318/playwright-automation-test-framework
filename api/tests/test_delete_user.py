import allure

from api.clients.reqres_client import ReqresClient



@allure.feature("User API")
@allure.story("Delete User")
def test_delete_user():


    client = ReqresClient()


    response = client.delete_user(2)


    assert response.status_code == 204