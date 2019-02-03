from .. matematica import fibonacci
from .. matematica import fibonacci_gen
import inspect
import math
import pytest


def test_fibonacci_value_error_se_non_intero():
    with pytest.raises(ValueError):
        fibonacci("42")


def test_fibonacci_value_error_se_minore_1():
    with pytest.raises(ValueError):
        fibonacci(0)


def test_fibonacci_di_10():
    assert fibonacci(10) == 55


def test_fibonacci_gen_is_generator_function():
    assert inspect.isgeneratorfunction(fibonacci_gen)


def test_fibonacci_gen_primi_5_valori():
    sucessione_fibonacci = fibonacci_gen()
    assert next(sucessione_fibonacci) == 1
    assert next(sucessione_fibonacci) == 1
    assert next(sucessione_fibonacci) == 2
    assert next(sucessione_fibonacci) == 3
    assert next(sucessione_fibonacci) == 5
