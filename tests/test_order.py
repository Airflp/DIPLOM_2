import allure

from data.user_data import TestUserData
from helpers.api_requests import get_ingredients, create_order_request


class TestCreateOrder:

    @staticmethod
    def get_ingredient_id():
        response = get_ingredients()
        return response.json()["data"][0]["_id"]

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_authorization(self, auth_user):
        _, access_token = auth_user
        ingredient_id = self.get_ingredient_id()

        response = create_order_request(
            ingredients=[ingredient_id],
            access_token=access_token
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization(self):
        ingredient_id = self.get_ingredient_id()

        response = create_order_request(
            ingredients=[ingredient_id]
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self):
        ingredient_id = self.get_ingredient_id()

        response = create_order_request(
            ingredients=[ingredient_id]
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = create_order_request(
            ingredients=[]
        )

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self):
        response = create_order_request(
            ingredients=[TestUserData.INVALID_INGREDIENT_HASH]
        )

        assert response.status_code == 400
        assert response.json()["success"] is False