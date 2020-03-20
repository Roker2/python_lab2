from math import sqrt


class Vector:

    def __init__(self, massive_one):
        self._coordinates = massive_one

    def __add__(self, other):
        print(str(self.get_dimension()) + '\n' + str(other.get_dimension()))
        if self.get_dimension() == other.get_dimension():
            new_coordinates = []
            for value_1, value_2 in zip(self._coordinates, other.get_coordinates()):
                new_coordinates.append(value_1 + value_2)
            return Vector(new_coordinates)
        else:
            print("Different dimensions.")

    def __sub__(self, other):
        if self.get_dimension() == other.get_dimension():
            new_coordinates = []
            for value_1, value_2 in zip(self._coordinates, other.get_coordinates()):
                new_coordinates.append(value_1 - value_2)
            return Vector(new_coordinates)
        else:
            print("Different dimensions.")

    def __mul__(self, other):
        if self.get_dimension() == other.get_dimension():
            result = 0
            for value_1, value_2 in zip(self._coordinates, other.get_coordinates()):
                result += value_1 * value_2
            return result

    def __str__(self):
        return str(self._coordinates)

    def __eq__(self, other):
        if self.get_dimension() != other.get_dimension():
            return False
        for value_1, value_2 in zip(self._coordinates, other.get_coordinates()):
            if value_2 != value_1:
                return False
        return True

    def __getitem__(self, key: int):
        return self._coordinates[key]

    def get_length(self):
        result = 0
        for value in self._coordinates:
            result += value * value
        return sqrt(result)

    def mul_number(self, number):
        massive = []
        for i in self._coordinates:
            massive.append(number * i)
        return Vector(massive)

    def get_coordinates(self):
        return self._coordinates

    def get_dimension(self):
        return len(self.get_coordinates())

    def set_coordinates(self, massive):
        if len(self._coordinates) == len(massive):
            self._coordinates = massive
        else:
            print("Different dimensions.")
