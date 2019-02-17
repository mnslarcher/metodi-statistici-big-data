from .. matematica import fibonacci
import math
import pytest


def test_value_error_se_n_non_intero():
    with pytest.raises(ValueError):
        fibonacci("42")


def test_value_error_se_n_minore_1():
    with pytest.raises(ValueError):
        fibonacci(0)


def test_n_uguale_10():
    assert fibonacci(10) == 55
