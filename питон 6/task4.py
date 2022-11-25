import json

INPUT_FILE = "input.csv"

def csv_to_list_dict():
    For_Keys = True
    keys = []
    value = []

    with open(INPUT_FILE) as file:
        for line in file.readlines():
            if For_Keys:
                keys = line.strip().split(',')
                For_Keys = False
            else:
                value.append(dict(zip(keys, line.strip().split(','))))
    return value

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))