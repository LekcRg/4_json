import json
import sys


def load_json(path_to_file):
    with open(path_to_file, "r") as file:
        return json.load(file)


def pretty_print_json(json_data):
    print(json.dumps(json_data, sort_keys=True, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    pretty_print_json(load_json(sys.argv[1]))
