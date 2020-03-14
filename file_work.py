def read_n_line(filename, n):
    with open(filename, "r") as file:
        for _ in range(1, n):
            file.readline()
        return file.readline()


def count_lines_in_file(filename, n=1):
    with open(filename, "r") as file:
        summa = sum(1 for line in file) - n + 1
    if summa < 0:
        return -1
    else:
        return summa
