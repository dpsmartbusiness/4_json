import json
import sys


def load_data(filepath):
    return json.loads(open(filepath, 'r').read())


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))


if __name__ == '__main__':
    filepath = sys.argv[1]
    pretty_print_json(load_data(sys.argv[1]))
pass
