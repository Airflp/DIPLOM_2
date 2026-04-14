import pytest

from helpers.user_generator import generate_user_data
from helpers.api_requests import register_user, login_user, delete_user


@pytest.fixture
def create_user():
    payload = generate_user_data()

    response = register_user(payload)

    access_token = None
    if response.status_code == 200 and response.json().get("success") is True:
        access_token = response.json().get("accessToken")

    yield payload, response

    if access_token:
        delete_user(access_token)


@pytest.fixture
def auth_user(create_user):
    payload, _ = create_user

    response = login_user(
        email=payload["email"],
        password=payload["password"]
    )

    access_token = response.json().get("accessToken")
    return payload, access_token