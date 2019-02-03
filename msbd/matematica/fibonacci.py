import numbers


def fibonacci(n):
    """Restituisce l'n-esimo numero della sucessione di Fibonacci.

    Vedere https://it.wikipedia.org/wiki/Successione_di_Fibonacci.

    Parameters
    ----------
    n : int
        Numero intero maggiore o uguale a 1.

    Returns
    -------
    fib : int
        N-esimo numero della sucessione di Fibonacci.
    """
    if not isinstance(n, numbers.Real) or not float(n).is_integer():
        raise ValueError("fibonacci() è definito solo per numeri interi.")
    elif n < 1:
        raise ValueError("fibonacci() è definito solo per valori maggiori o "
            "uguali a 1.")
    else:
        if n <= 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_gen():
    """Sucessione di Fibonacci.

    Vedere https://it.wikipedia.org/wiki/Successione_di_Fibonacci.

    Returns
    -------
    fib_gen : generator
        Generatore della sucessione di Fibonacci.
    """
    f1, f2 = 1, 1
    it = 0

    while True:
        if it < 2:
            it += 1
            yield 1
        else:
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            yield f3
