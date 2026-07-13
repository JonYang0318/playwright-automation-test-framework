import allure

from api.clients.reqres_client import ReqresClient


@allure.feature("User API")
@allure.story("Create User")
def test_create_user():


    client = ReqresClient()


    payload = {

        "name": "Jimmy",

        "job": "QA Engineer"

    }


    response = client.create_user(payload)


    assert response.status_code == 201


    body = response.json()


    assert body["name"] == "Jimmy"

    assert body["job"] == "QA Engineer"

    assert "id" in body

    assert "createdAt" in body