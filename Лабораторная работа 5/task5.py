import random
import string


def get_random_password() -> str:
    return random.sample(string.digits + string.ascii_lowercase + string.ascii_uppercase, k=8)


print(get_random_password())
