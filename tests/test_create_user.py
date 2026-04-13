import allure
import requests

from data.user_data import BASE_URL, REGISTER_ENDPOINT
from helpers.user_generator import generate_user_data


class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        payload = generate_user_data()

        response = requests.post(
            f"{BASE_URL}{REGISTER_ENDPOINT}",
            json=payload
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

        requests.delete(
            f"{BASE_URL}/auth/user",
            headers={"Authorization": response.json()["accessToken"]}
        )

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_already_registered_user(self, create_user):
        payload, access_token = create_user

        response = requests.post(
            f"{BASE_URL}{REGISTER_ENDPOINT}",
            json=payload
        )

        assert response.status_code == 403
        assert response.json()["success"] is False

    @allure.title("Создание пользователя без обязательного поля")
    @allure.description("Проверка без email")
    def test_create_user_without_required_field(self):
        payload = generate_user_data()
        del payload["email"]

        response = requests.post(
            f"{BASE_URL}{REGISTER_ENDPOINT}",
            json=payload
        )

        assert response.status_code == 403
        assert response.json()["success"] is False