import matplotlib.pyplot as plt
import pandas as pd


def grafico_coefficienti(coefficienti, variabili):
    """Grafico dei coefficienti

    Parameters
    ----------
    coefficienti : array-like
        Valori dei coefficienti.
    variabili : array-like
        Nomi delle variabili legate ai coefficienti.

    """
    coef = pd.Series(coefficienti, variabili).sort_values()
    coef.plot(kind='bar', title='Grafico dei coefficienti',
        color=[["tab:blue", "tab:orange"][i] for i in (coef > 0)])
    plt.grid()
