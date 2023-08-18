import ctypes


class DynamicArray:

    def __init__(self):

        self.n = 0  # Initial array number of elements
        self.capacity = 1  # initial array capacity
        self.A = self.create_array(self.capacity)

    def __getitem__(self, item):
        return self.A[item]

    def __setitem__(self, key, value):
        self.A[self.n] = value
        self.n += 1

    def __len__(self):
        return self.n

    def append(self, value):
        if self.capacity == self.n:
            self.capacity = self.capacity * 2
            self.resize()
        self.A[self.n] = value
        self.n += 1

    def resize(self):
        b = self.create_array(self.capacity)

        for i in range(self.n):
            b[i] = self.A[i]

        self.A = b
        del b

    @staticmethod
    def create_array(new_capacity):
        return (new_capacity * ctypes.py_object)()
