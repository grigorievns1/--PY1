import json
INPUT_FILE = "input.csv"
def csv_to_list_dict(input_file):
    value = []

    with open(input_file) as file:
        keys = file.readline().strip().split(',')
        for line in file:
            value.append(dict(zip(keys, line.strip().split(','))))
    return value

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))