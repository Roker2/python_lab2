def merge(left_data, right_data):
    sorted_data = []
    left_index = 0
    right_index = 0
    for _ in range(len(left_data) + len(right_data)):
        if (left_index < len(left_data)) & (right_index < len(right_data)):
            if left_data[left_index] <= right_data[right_index]:
                sorted_data.append(left_data[left_index])
                left_index += 1
            else:
                sorted_data.append(right_data[right_index])
                right_index += 1
        elif left_index == len(left_data):
            sorted_data.append(right_data[right_index])
            right_index += 1
        elif right_index == len(right_data):
            sorted_data.append(left_data[left_index])
            left_index += 1
    return sorted_data


def merge_sort(data):
    if len(data) <= 1:
        return data
    center = len(data) // 2
    return merge(merge_sort(data[:center]),
                 merge_sort(data[center:]))


def read_n_line(filename, n):
    with open(filename, "r") as file:
        for _ in range (1, n):
            file.readline()
        return file.readline()


def count_lines_in_file(filename):
    file = open(filename)
    return sum(1 for line in file)
