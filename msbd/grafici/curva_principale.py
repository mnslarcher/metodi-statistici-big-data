import matplotlib.pyplot as plt
import numpy as np


def grafico_curva_principale(X, cp):
    plt.scatter(X[:, 0], X[:, 1], facecolor="none",
        edgecolor="tab:blue", label="Osservazioni")
    plt.plot(cp.f1_hat(np.array(sorted(cp.l_hat))),
        cp.f2_hat(np.array(sorted(cp.l_hat))),
        color="tab:orange", lw=2, label="Curva principale")

    for i in range(len(X)):
        plt.plot([X[i, 0], cp.X_prz[i, 0]], [X[i, 1], cp.X_prz[i, 1]],
            c="tab:gray", ls="--", alpha=0.5)

    plt.scatter(cp.X_prz[:, 0], cp.X_prz[:, 1],
        label="Proiezione delle osservazioni sulla curva principale",
        color="tab:blue")
