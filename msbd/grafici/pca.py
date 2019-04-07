import matplotlib.pyplot as plt
import numpy as np


def grafico_varianza_spiegata(varianza_spiegata, cumulata=False):
    titolo = "% varianza spiegata"

    if cumulata:
        titolo += " cumulata al variare del numero di componenti"
        varianza_spiegata = varianza_spiegata.cumsum()
    else:
        titolo += " da ogni componente"

    plt.title(titolo)
    plt.plot(range(1, len(varianza_spiegata) + 1), varianza_spiegata,
        marker='o', ls='--')
    plt.xlabel("Componenti")
    plt.ylabel("% varianza spiegata")
    plt.grid()


def grafico_proiezione_sul_primo_asse_principale(X):
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    V = Vt.T
    V1 = V[:, [0]]
    H1 = V1.dot(V1.T)
    X1 = X.dot(H1)

    x_max, y_max = np.max([-X.min(axis=0), X.max(axis=0)], axis=0) * 1.1
    x = np.linspace(-x_max, x_max)

    plt.title("Proiezione di X sul primo asse principale")
    plt.scatter(X[:, 0], X[:, 1], facecolor="none", edgecolor="tab:blue",
        label="$x_i$")
    plt.scatter(X1[:, 0], X1[:, 1], color="tab:blue",
        label="$\mathbf{H_1}x_i$")
    plt.plot(x, x * V1[1] / V1[0], ls="--", color="tab:orange",
        label="Primo asse principale")
    plt.arrow(0, 0, V1[0, 0], V1[1, 0], head_width=0.2, lw=2, color="tab:orange")
    plt.hlines(0, -x_max, x_max)
    plt.vlines(0, -y_max, y_max)
    plt.xlim([-x_max, x_max])
    plt.ylim([-y_max, y_max])
    plt.legend()
