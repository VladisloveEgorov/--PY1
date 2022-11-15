import random
import string


def get_random_password(length) -> str:
    return random.sample(string.digits + string.ascii_lowercase + string.ascii_uppercase, k=length)


print(get_random_password(8))
