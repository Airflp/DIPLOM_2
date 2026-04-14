import allure

from data.user_data import TestUserData
from helpers.api_requests import login_user


class TestLoginUser:

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, create_user):
        payload, _ = create_user

        response = login_user(
            email=payload["email"],
            password=payload["password"]
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Логин с неверным логином и паролем")
    def test_login_with_invalid_credentials(self):
        response = login_user(
            email=TestUserData.INVALID_EMAIL,
            password=TestUserData.INVALID_PASSWORD
        )

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == "email or password are incorrect"