class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru/api"

    REGISTER_ENDPOINT = "/auth/register"
    LOGIN_ENDPOINT = "/auth/login"
    USER_ENDPOINT = "/auth/user"
    ORDERS_ENDPOINT = "/orders"
    INGREDIENTS_ENDPOINT = "/ingredients"


class TestUserData:
    DEFAULT_PASSWORD = "Qwerty26"
    DEFAULT_NAME = "arturkozlov41"
    INVALID_EMAIL = "wrong_user@yandex.ru"
    INVALID_PASSWORD = "wrong_password"
    INVALID_INGREDIENT_HASH = "invalid_hash"