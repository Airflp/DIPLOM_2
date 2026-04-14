import allure
import requests

from data.user_data import Urls


@allure.step("Регистрация нового пользователя")
def register_user(payload):
    return requests.post(
        f"{Urls.BASE_URL}{Urls.REGISTER_ENDPOINT}",
        json=payload
    )


@allure.step("Авторизация пользователя")
def login_user(email, password):
    return requests.post(
        f"{Urls.BASE_URL}{Urls.LOGIN_ENDPOINT}",
        json={
            "email": email,
            "password": password
        }
    )


@allure.step("Удаление пользователя")
def delete_user(access_token):
    return requests.delete(
        f"{Urls.BASE_URL}{Urls.USER_ENDPOINT}",
        headers={"Authorization": access_token}
    )


@allure.step("Получение списка ингредиентов")
def get_ingredients():
    return requests.get(
        f"{Urls.BASE_URL}{Urls.INGREDIENTS_ENDPOINT}"
    )


@allure.step("Создание заказа")
def create_order_request(ingredients, access_token=None):
    headers = {}
    if access_token:
        headers["Authorization"] = access_token

    return requests.post(
        f"{Urls.BASE_URL}{Urls.ORDERS_ENDPOINT}",
        json={"ingredients": ingredients},
        headers=headers
    )