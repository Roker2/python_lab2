import argparse
import random
import to_json
import sorting_by_merges
import math
import os
from pathlib import Path
import vector
import unittest
import file_work


class SortingTest(unittest.TestCase):
    def test_it_can_be_sorted(self):
        """
        test_massive = []
        with open('test.txt', 'w') as f:
            for _ in range(int(100)):
                random_digit = random.randint(-1000000, 1000000)
                test_massive.append(random_digit)
                f.writelines('{}\n'.format(random_digit))
        """
        with open('test.txt', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(int(100)))
            f.write('Hey')
        with self.assertRaises(Exception):
            sorting_by_merges.sort_merge('test.txt')

    def test_is_sorted(self):
        with open('test.txt', 'w') as f:
            f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(int(100)))
        sorting_by_merges.sort_merge('test.txt')
        massive = []
        lines_count = file_work.count_lines_in_file('sorted.txt')
        for i in range(lines_count):
            massive.append(int(file_work.read_n_line('sorted.txt', i)))
        self.assertEqual(sorted(massive), massive)


class CachedTest(unittest.TestCase):
    def test_right_answer(self):
        self.assertEqual(int(plus_four_digits(1, 2, 3, 4)), 10)

    def test_file_exist(self):
        os.mkdir("./cache/file.txt")
        with self.assertRaises(IsADirectoryError):
            print(plus_four_digits(1, 2, 3, 4))
        os.removedirs("./cache/file.txt")


def cached(func):
    def wrapper(*args):
        cache_folder = "./cache"
        if not Path(cache_folder).is_dir():
            os.mkdir(cache_folder)
        filename = "cache/file.txt"
        if Path(filename).is_file():
            with open(filename, "r") as file:
                for _ in range(0, file_work.count_lines_in_file(filename)):
                    temp_list = file.readline().split()
                    # print(temp_list)
                    if len(args) == len(temp_list) - 1:
                        for i in range(0, len(args)):
                            if str(args[i]) != temp_list[i]:
                                break
                        else:
                            print("Found!")
                            return temp_list[len(temp_list) - 1]
        string_cache = ''
        if Path(filename).is_file():
            with open(filename, "r") as file:
                for _ in range(0, file_work.count_lines_in_file(filename)):
                    string_cache += file.readline()
        for i in range(0, len(args)):
            string_cache += str(args[i]) + ' '
        returned = func(*args)
        string_cache += str(returned) + '\n'
        with open(filename, "w") as file:
            file.write(string_cache)
        print("Saved")
        return returned
    return wrapper


@cached
def plus_and_pow(a, b, n):
    return math.pow(a + b, n)


@cached
def plus_four_digits(a, b, c, d):
    return a + b + c + d


def generate_file(quantity='500000000'):
    with open('numbers.txt', 'w') as f:
        f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(int(quantity)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, help='Type program: one, two, three, four, five')
    parser.add_argument('-g', '--generate_file', type=generate_file)

    if vars(parser.parse_args())['type'] == 'two':
        MyDict = {"one": 1, "second": "LOL", "massiv": [555, 666], "Dict2": {"heh": 555, "kek": "lol"}, "bool": True}
        print(MyDict)
        print(to_json.obj_to_json(MyDict))
    if vars(parser.parse_args())['type'] == 'one':
        sorting_by_merges.sort_merge("numbers.txt")
    if vars(parser.parse_args())['type'] == 'four':
        print(plus_and_pow(2, 3, 100))
        print(plus_and_pow(2, 3, 3))
        print(plus_four_digits(1, 2, 3, 4))
    if vars(parser.parse_args())['type'] == 'three':
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
    unittest.main()
