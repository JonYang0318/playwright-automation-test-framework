import allure

from jsonschema import validate

from api.clients.reqres_client import ReqresClient
from api.schemas.user_schema import user_schema



@allure.title("Get User")
def test_get_user():

    client = ReqresClient()

    response = client.get_user(2)


    assert response.status_code == 200


    body = response.json()


    validate(
        instance=body,
        schema=user_schema
    )


    assert body["data"]["id"] == 2