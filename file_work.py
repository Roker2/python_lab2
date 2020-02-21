"""
def sort_merge(filename):
    i = 1
    n = 1
    count = count_lines_in_file(filename)
    remainder = count % n
    left_index =
"""


def read_n_line(filename, n):
    with open(filename, "r") as file:
        for _ in range (1, n):
            file.readline()
        return file.readline()


def count_lines_in_file(filename, n=1):
    file = open(filename)
    summa = sum(1 for line in file) - n + 1
    if summa < 0:
        return -1
    else:
        return summa
