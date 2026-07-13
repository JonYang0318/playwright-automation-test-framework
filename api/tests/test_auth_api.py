import allure

from api.clients.auth_client import AuthClient



@allure.feature("Authentication API")
@allure.story("Login Success")
def test_login_success():


    client = AuthClient()


    payload = {

        "email": "eve.holt@reqres.in",

        "password": "cityslicka"

    }


    response = client.login(payload)


    assert response.status_code == 200


    body = response.json()


    assert "token" in body

    assert body["token"] is not None

@allure.story("Login Failed")
def test_login_failed():


    client = AuthClient()


    payload = {

        "email": "peter@klaven"

    }


    response = client.login(payload)


    assert response.status_code == 400


    body = response.json()


    assert body["error"] == "Missing password"