import allure
import requests

from data.user_data import BASE_URL, ORDERS_ENDPOINT, INGREDIENTS_ENDPOINT


class TestCreateOrder:

    def get_ingredient_id(self):
        response = requests.get(f"{BASE_URL}{INGREDIENTS_ENDPOINT}")
        return response.json()["data"][0]["_id"]

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_authorization(self, auth_user):
        _, access_token = auth_user
        ingredient_id = self.get_ingredient_id()

        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            json={"ingredients": [ingredient_id]},
            headers={"Authorization": access_token}
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization(self):
        ingredient_id = self.get_ingredient_id()

        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            json={"ingredients": [ingredient_id]}
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self):
        ingredient_id = self.get_ingredient_id()

        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            json={"ingredients": [ingredient_id]}
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            json={"ingredients": []}
        )

        assert response.status_code == 400
        assert response.json()["success"] is False

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_ingredient_hash(self):
        response = requests.post(
            f"{BASE_URL}{ORDERS_ENDPOINT}",
            json={"ingredients": ["invalid_hash"]}
        )

        assert response.status_code == 400
        assert response.json()["success"] is False