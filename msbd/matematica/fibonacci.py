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
