import json


def load_data(path_to_file):
    return pretty_print_json(json.load(open(path_to_file, "r")))


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    pass


load_data(input())
