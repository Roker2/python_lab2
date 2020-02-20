import argparse
import random


def generate_file(quantity=500000000):
    with open('numbers.txt', 'w') as f:
        f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(quantity))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, help='Type program: one, two, three, four, five, generate_file')

    if vars(parser.parse_args())['type'] == 'generate_file':
        generate_file(50)
