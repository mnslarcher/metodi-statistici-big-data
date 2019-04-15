import math
import numpy as np


class CocktailParty:
    """Problema del cocktail party"""

    def __init__(self, A):
        self.A = A

    def s1(self, t):
        return 2 * np.sin(math.pi * t / 8)

    def s2(self, t):
        return 1 / 5 * (t % (5 * 4 + 1)) - 2

    def x1(self, t):
        return self.A[0, 0] * self.s1(t) + self.A[0, 1] * self.s2(t)

    def x2(self, t):
        return self.A[1, 0] * self.s1(t) + self.A[1, 1] * self.s2(t)
