import argparse
import random
import to_json
import sorting_by_merges
import math
import os
from pathlib import Path
import vector


def count_lines_in_file(filename, n=1):
    file = open(filename)
    summa = sum(1 for line in file) - n + 1
    if summa < 0:
        return -1
    else:
        return summa


def cached(func):
    def wrapper(arg1, arg2, arg3):
        cache_folder = "./cache"
        if not Path(cache_folder).is_dir():
            os.mkdir(cache_folder)
        filename = "cache/file.txt"
        if Path(filename).is_file():
            with open(filename, "r") as file:
                for _ in range(0, count_lines_in_file(filename)):
                    temp_list = file.readline().split()
                    # print(temp_list)
                    if (str(arg1) == temp_list[0]) & (str(arg2) == temp_list[1]) & (str(arg3) == temp_list[2]):
                        print("Found!")
                        return float(temp_list[3])
        string_cache = ''
        if Path(filename).is_file():
            with open(filename, "r") as file:
                for _ in range(0, count_lines_in_file(filename)):
                    string_cache += file.readline()
        string_cache += str(arg1) + ' ' + str(arg2) + ' ' + str(arg3) + ' '
        returned = func(arg1, arg2, arg3)
        string_cache += str(returned) + '\n'
        with open(filename, "w") as file:
            file.write(string_cache)
        print("Saved")
        return returned
    return wrapper


@cached
def plus_and_pow(a, b, n):
    return math.pow(a + b, n)


def generate_file(quantity='500000000', filename="numbers.txt"):
    with open(filename, 'w') as f:
        f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(int(quantity)))


def program_one(filename="numbers.txt"):
    sorting_by_merges.sort_merge(filename)


def program_two():
    MyDict = {"one": 1, "second": "LOL", "massiv": [555, 666], "Dict2": {"heh": 555, "kek": "lol"}, "bool": True}
    print(MyDict)
    print(to_json.obj_to_json(MyDict))


def program_three():
    test1 = vector.Vector([5, 5])
    test2 = vector.Vector([5, 5])
    print(test1)
    print(test2 + test1)
    print(test2 - test1)
    print(test2 * test1)
    print(test1.mul_number(5))
    print(test1 == test2)
    print(test1.get_length())
    print(test1[0])


def program_four():
    print(plus_and_pow(2, 3, 100))
    print(plus_and_pow(2, 3, 3))


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-g', '--generate_file', type=generate_file)
    parser.add_argument('--one', type=program_one)
    parser.add_argument('--two', type=program_two)
    parser.add_argument('--three', type=program_three)
    parser.add_argument('--four', type=program_four)
    print(parser.parse_args())
    return parser.parse_args()


if __name__ == '__main__':
    main()
