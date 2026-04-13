import random
import string

from data.user_data import DEFAULT_NAME, DEFAULT_PASSWORD


def generate_random_string(length=8):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def generate_user_data():
    random_part = generate_random_string()
    return {
        "email": f"test_{random_part}@yandex.ru",
        "password": DEFAULT_PASSWORD,
        "name": DEFAULT_NAME
    }