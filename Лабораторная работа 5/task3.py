import random


def get_unique_list_numbers(start, stop, num) -> list[int]:
    list_ = []
    while len(list_) < num:
        x = random.randint(start, stop)
        if x not in list_:
            list_.append(x)
    return list_


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
