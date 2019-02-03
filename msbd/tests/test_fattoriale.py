from ..matematica import fattoriale
import math


def test_fattoriale_di_zero():
    assert fattoriale(0) == 1


def test_fattoriale_di_quarantadue():
    assert fattoriale(42) == math.factorial(42)
