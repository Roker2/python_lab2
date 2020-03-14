import file_work
import os


def sort_merge(filename):
    n = 1
    count = file_work.count_lines_in_file(filename)
    orig_filename = filename
    left_index = 0
    right_index = 0
    while n <= count:
        i = 1
        file = open("sorted" + str(n) + ".txt", "w")
        while i <= count:
            """
            print("i=" + str(i))
            print("i + right_index + n=" + str(i + right_index + n) + ": " + file_work.read_n_line(filename, i + right_index + n))
            print("i + left_index=" + str(i + left_index) + ": " + file_work.read_n_line(filename, i + left_index) + '\n')
            """
            for _ in range(n * 2):
                if file_work.read_n_line(filename, i + left_index) == '':
                    continue
                elif file_work.read_n_line(filename, i + right_index + n) == '':
                    right_index = n
                if (left_index < n) & (right_index < n):
                    if int(file_work.read_n_line(filename, i + left_index)) <= int(file_work.read_n_line(filename, i + right_index + n)):
                        file.write(file_work.read_n_line(filename, i + left_index))
                        left_index += 1
                    else:
                        file.write(file_work.read_n_line(filename, i + right_index + n))
                        right_index += 1
                elif left_index == n:
                    file.write(file_work.read_n_line(filename, i + right_index + n))
                    right_index += 1
                elif right_index == n:
                    file.write(file_work.read_n_line(filename, i + left_index))
                    left_index += 1
            i += n * 2
            left_index = 0
            right_index = 0
        file.close()
        if filename != orig_filename:
            os.remove(filename)
        filename = file.name
        n *= 2
    os.rename("sorted" + str(n // 2) + ".txt", "sorted.txt")
