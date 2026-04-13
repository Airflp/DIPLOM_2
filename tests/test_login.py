import allure
import requests

from data.user_data import BASE_URL, LOGIN_ENDPOINT


class TestLoginUser:

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, create_user):
        payload, _ = create_user

        response = requests.post(
            f"{BASE_URL}{LOGIN_ENDPOINT}",
            json={
                "email": payload["email"],
                "password": payload["password"]
            }
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Логин с неверным логином и паролем")
    def test_login_with_invalid_credentials(self):
        response = requests.post(
            f"{BASE_URL}{LOGIN_ENDPOINT}",
            json={
                "email": "wrong_user@yandex.ru",
                "password": "wrong_password"
            }
        )

        assert response.status_code == 401
        assert response.json()["success"] is False