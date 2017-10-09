import json


def load_data(path_to_file):
    with open(path_to_file, "r") as f:
        return json.load(f)


def pretty_print_json(json_data):
    return json.dumps(json_data, sort_keys=True, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print(pretty_print_json(load_data(input())))
