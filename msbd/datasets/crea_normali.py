from sklearn.utils import shuffle
import numpy as np


def crea_normali(medie, cov, num):
    X = np.empty((0, 2), dtype=float)
    y = np.empty((0,), dtype=float)

    for i, (m, c, n) in enumerate(zip(medie, cov, num)):
        X = np.append(X, np.random.multivariate_normal(mean=m, cov=c, size=n),
            axis=0)
        y = np.append(y, i * np.ones(n, dtype=int))

    X, y = shuffle(X, y)

    return X, y
