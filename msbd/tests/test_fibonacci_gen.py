from .. matematica import fibonacci_gen
import inspect


def test_e_funzione_generatore():
    assert inspect.isgeneratorfunction(fibonacci_gen)


def test_primi_5_valori_generati():
    fib = fibonacci_gen()
    assert next(fib) == 1
    assert next(fib) == 1
    assert next(fib) == 2
    assert next(fib) == 3
    assert next(fib) == 5
