import numpy as np


class Matrix:
    def __init__(self, data):
        if not isinstance(data, np.ndarray):
            raise ValueError("Wrong input")
        self.data = data

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong shape")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Wrong shape")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Wrong shape")
        return Matrix(self.data @ other.data)

    def save_to_text_file(self, file):
        with open(file, "w") as f:
            f.write(str(self.data))


if __name__ == '__main__':
    np.random.seed(0)
    a = Matrix(np.random.randint(0, 10, (10, 10)))
    b = Matrix(np.random.randint(0, 10, (10, 10)))

    matrix_add = a + b
    matrix_mul = a * b
    matrix_matmul = a @ b

    matrix_add.save_to_text_file("./artifacts/3.1/matrix+.txt")
    matrix_mul.save_to_text_file("./artifacts/3.1/matrix*.txt")
    matrix_matmul.save_to_text_file("./artifacts/3.1/matrix@.txt")
