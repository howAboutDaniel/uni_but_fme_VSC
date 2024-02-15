import keras

import numpy as np

# vstupy 2, 3; nulty vstup 1 pro bias
x = np.array([1, 2, 3])
# prvni radek w je bias
w = np.array([[1, 0.5, 1], [2, -1, -0.4]]).transpose()
print(x)
print(w)
print(x @ w)  # np.matmul(x, w)

# mozna neni uplne dobre
class Layer:
    def __init__(self, w: np.ndarray, b: np.ndarray):
        self.w = np.vstack(b, w)

    def apply(self, x: np.ndarray):
        xx = np.hstack((1, x))
        return np.tanh(xx @ self.w)
