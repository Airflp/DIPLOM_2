import pytest
import requests

from data.user_data import (
    BASE_URL,
    REGISTER_ENDPOINT,
    LOGIN_ENDPOINT,
    USER_ENDPOINT
)
from helpers.user_generator import generate_user_data


@pytest.fixture
def create_user():
    payload = generate_user_data()

    response = requests.post(
        f"{BASE_URL}{REGISTER_ENDPOINT}",
        json=payload
    )

    access_token = None
    if response.status_code == 200 and response.json().get("success") is True:
        access_token = response.json().get("accessToken")

    yield payload, access_token

    if access_token:
        requests.delete(
            f"{BASE_URL}{USER_ENDPOINT}",
            headers={"Authorization": access_token}
        )


@pytest.fixture
def auth_user(create_user):
    payload, _ = create_user

    response = requests.post(
        f"{BASE_URL}{LOGIN_ENDPOINT}",
        json={
            "email": payload["email"],
            "password": payload["password"]
        }
    )

    access_token = response.json().get("accessToken")
    yield payload, access_token