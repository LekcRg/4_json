import json
import sys


def do_data_json(path_to_file):
    with open(path_to_file, "r") as file:
        return json.load(file)


def pretty_print_json(json_data):
    return json.dumps(json_data, sort_keys=True, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print(pretty_print_json(do_data_json(sys.argv[1])))
