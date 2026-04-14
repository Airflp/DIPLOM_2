import allure

from helpers.user_generator import generate_user_data
from helpers.api_requests import register_user


class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, create_user):
        _, response = create_user

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_already_registered_user(self, create_user):
        payload, _ = create_user

        response = register_user(payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    @allure.description("Проверка создания пользователя без email")
    def test_create_user_without_required_field(self):
        payload = generate_user_data()
        del payload["email"]

        response = register_user(payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "Email, password and name are required fields"