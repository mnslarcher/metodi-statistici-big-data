import numpy as np


class SpiraleLogaritmica:
    """Spirale logaritimica."""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def f1(self, l):
        return self.a * np.exp(self.b * l) * np.cos(l)

    def f2(self, l):
        return self.a * np.exp(self.b * l) * np.sin(l)

    def f(self, l):
        return np.c_[self.f1(l), self.f2(l)]
