import math
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def grafico_barre_qualitative_risposta(X, y, qualitative, n_columns):
    """Grafico a barre della relazione tra qualitative e risposta"""
    n_var = len(qualitative)

    for i, var in enumerate(qualitative):
        ax = plt.subplot(math.ceil(n_var / n_columns), n_columns, i + 1)
        pd.concat([X[var], y], axis=1).groupby(var).mean().plot(ax=ax,
            kind='bar')
        plt.tight_layout()
        plt.grid()


def grafico_dispersione_quantitative_risposta(X, y, quantitative, n_columns):
    """Grafici di dispersione tra quantitative e risposta"""
    n_var = len(quantitative)

    for i, var in enumerate(quantitative):
        plt.subplot(math.ceil(n_var / n_columns), n_columns, i + 1)
        sns.regplot(X[var], y=y, line_kws={"color": "orange", "ls": "--"})
        plt.tight_layout()
        plt.grid()
