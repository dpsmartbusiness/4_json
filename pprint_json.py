import json
import sys


def load_data(filepath):
     with open(filepath,'r') as opened_file:
        unstructured_data = json.loads(opened_file.read())
     return unstructured_data


def pretty_print_json(unstructured_data):
    print(json.dumps(unstructured_data, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))


if __name__ == '__main__':
    filepath = sys.argv[1]
    pretty_print_json(load_data(sys.argv[1]))
