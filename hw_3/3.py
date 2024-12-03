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


class HashMixin:
    def __hash__(self):
        # Произведение хешей строк матрицы
        return hash(tuple(hash(tuple(row)) for row in self.data))


class MatrixWithHash(Matrix, HashMixin):
    _cache = {}

    def __matmul__(self, other):
        key = (hash(self), hash(other))
        if key in self._cache:
            return self._cache[key]
        result = super().__matmul__(other)
        self._cache[key] = result
        return result


if __name__ == '__main__':
    a = MatrixWithHash(np.random.randint(0, 100, (2, 2)))
    b = MatrixWithHash(np.random.randint(0, 100, (2, 2)))
    c = MatrixWithHash(np.random.randint(0, 100, (2, 2)))
    d = MatrixWithHash(b.data.copy())
    count = 0

    while not (hash(a) == hash(c)
               and not np.array_equal(a.data, c.data)
               and np.array_equal(b.data, d.data)
               and not np.array_equal((a @ b).data, (c @ d).data)):
        a = MatrixWithHash(np.random.randint(0, 100, (2, 2)))
        c = MatrixWithHash(np.random.randint(0, 100, (2, 2)))
        b = MatrixWithHash(np.random.randint(0, 100, (2, 2)))
        d = MatrixWithHash(b.data.copy())

        count += 1
        print(f"Trying to find collision, try #{count}")

    a.save_to_text_file("./artifacts/3.3/A.txt")
    b.save_to_text_file("./artifacts/3.3/B.txt")
    c.save_to_text_file("./artifacts/3.3/C.txt")
    d.save_to_text_file("./artifacts/3.3/D.txt")

    (a @ b).save_to_text_file("./artifacts/3.3/AB.txt")
    (c @ d).save_to_text_file("./artifacts/3.3/CD.txt")

    with open("./artifacts/3.3/hash.txt", "w") as f:
        f.write(f"hash(A @ B) = {hash(a @ b)}\n")
        f.write(f"hash(C @ D) = {hash(c @ d)}\n")
