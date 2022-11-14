import random


def get_unique_list_numbers() -> list[int]:
    n = 16
    list_ = [random.randint(-10, 10) for _ in range(n)]
    list_new = []
    for x in list_:
        if x not in list_new:
            list_new.append(x)
    return list_new


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
