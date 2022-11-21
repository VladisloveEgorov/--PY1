import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    list_ = []
    with open(file) as f:
        header = f.readline().strip().split(',')
        for line in f:
            list_.append(dict(zip(header, line.strip().split(','))))
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
