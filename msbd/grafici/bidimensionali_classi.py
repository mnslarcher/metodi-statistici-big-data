from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def grafico_bidimensionale_classi(X, y, alpha=None, s=None, cm=plt.cm.tab10):
    for i in sorted(np.unique(y.astype(int))):
        plt.scatter(X[y == i, 0], X[y == i, 1], color=cm(i), alpha=alpha, s=s,
                    label="Classe {}".format(i))


def grafico_bidimensionale_classi_previste(X_train, y_train, X_val, y_val,
        y_pred, nome_clf, alpha=1., s=75, cm=plt.cm.tab10):
    plt.title("Classi previste (accuratezza {}: {:.2f}%)".format(nome_clf, 100 *
        accuracy_score(y_val, y_pred)))

    grafico_bidimensionale_classi(X_train, y_train, alpha=alpha / 3, s=s / 3,
        cm=cm)
    grafico_bidimensionale_classi(X_val, y_val, alpha=alpha, s=s, cm=cm)

    for x, y in zip(X_val, y_pred.astype(int)):
        plt.text(x[0], x[1], y, color="black", fontsize=16)

    plt.legend(["Classe {} ({})".format(c, t) for t in ["train", "val"] for c
        in np.unique(y_train.astype(int))])
