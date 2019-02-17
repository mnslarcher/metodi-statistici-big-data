from ..matematica import fattoriale
import math
import pytest


def test_value_error_se_n_non_intero():
    with pytest.raises(ValueError):
        fattoriale("42")


def test_value_error_se_n_minore_0():
    with pytest.raises(ValueError):
        fattoriale(-1)


def test_n_uguale_0():
    assert fattoriale(0) == 1


def test_n_uguale_42():
    assert fattoriale(42) == math.factorial(42)
