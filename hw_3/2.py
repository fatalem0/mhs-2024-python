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


class MatrixMixin:
    @property
    def shape(self):
        return self.data.shape

    @shape.setter
    def shape(self, new_shape):
        self.data = self.data.reshape(new_shape)

    def save_to_text_file(self, file):
        with open(file, "w") as f:
            f.write(str(self.data))

    def __str__(self):
        return np.array2string(self.data)


class Matrix2(Matrix, MatrixMixin):
    pass


if __name__ == '__main__':
    np.random.seed(0)
    a = Matrix2(np.random.randint(0, 10, (10, 10)))
    b = Matrix2(np.random.randint(0, 10, (10, 10)))

    matrix_add = a + b
    matrix_mul = a * b
    matrix_matmul = a @ b

    matrix_add.save_to_text_file("./artifacts/3.2/matrix+.txt")
    matrix_mul.save_to_text_file("./artifacts/3.2/matrix*.txt")
    matrix_matmul.save_to_text_file("./artifacts/3.2/matrix@.txt")
