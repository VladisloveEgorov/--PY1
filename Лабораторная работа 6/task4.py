import csv
import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    list_ = []
    with open(file) as f:
        cond = True
        for line in f:
            if cond:
                key = line.strip().split(',')
                cond = False
            else:
                list_.append({key[i]: line.strip().split(',')[i] for i in range(len(key))})
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
