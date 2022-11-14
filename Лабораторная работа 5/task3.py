import random


def get_unique_list_numbers(start, stop, num) -> list[int]:
    list_ = [random.randint(start, stop) for _ in range(num)]
    list_new = []
    for x in list_:
        if x not in list_new:
            list_new.append(x)
    return list_new


list_unique_numbers = get_unique_list_numbers(-10, 10, 16)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
