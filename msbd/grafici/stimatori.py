import matplotlib.pyplot as plt
import pandas as pd


def grafico_coefficienti(coef, nomi):
    """Grafico dei coefficienti

    Parameters
    ----------
    coef : array-like
        Valori dei coefficienti.
    nomi : array-like
        Nomi delle variabili legate ai coefficienti.

    """
    coef = pd.Series(coef, nomi).sort_values()
    coef.plot(kind='bar', title='Grafico dei coefficienti',
        color=[["tab:blue", "tab:orange"][i] for i in (coef > 0)])
    plt.grid()
