import argparse
import random
import to_json
import sorting_by_merges
import math


def plus_and_pow(a, b, n):
    return math.pow(a + b, n)


def generate_file(quantity='500000000'):
    with open('numbers.txt', 'w') as f:
        f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(int(quantity)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, help='Type program: one, two, three, four, five, generate_file')
    parser.add_argument('-g', '--generate_file', type= generate_file)

    if vars(parser.parse_args())['type'] == 'generate_file':
        generate_file("50")
    if vars(parser.parse_args())['type'] == 'two':
        MyDict = {"one": 1, "second": "LOL", "massiv": [555, 666], "Dict2": {"heh": 555, "kek": "lol"}, "bool": True}
        print(MyDict)
        print(to_json.obj_to_json(MyDict))
    if vars(parser.parse_args())['type'] == 'one':
        sorting_by_merges.sort_merge("numbers.txt")
