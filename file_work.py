def read_n_line(filename, n):
    with open(filename, "r") as file:
        for _ in range(1, n):
            file.readline()
        return file.readline()


def count_lines_in_file(filename, n=1):
    with open(filename, "r") as file:
        lines_count = sum(1 for line in file) - n + 1
    if lines_count < 0:
        return -1
    else:
        return lines_count
