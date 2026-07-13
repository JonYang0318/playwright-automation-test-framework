import allure
from api.clients.reqres_client import ReqresClient
import requests


def test_without_api_key():

    response = requests.get(
        "https://reqres.in/api/users/2"
    )

    assert response.status_code == 401