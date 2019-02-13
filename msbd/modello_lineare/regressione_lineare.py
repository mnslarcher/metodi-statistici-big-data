import numpy as np


class RegressioneLineare():
    """Regressione lineare.

    Vedere https://it.wikipedia.org/wiki/Regressione_lineare.

    Parameters
    ----------
    fit_intercept : boolean, optional, default True
        Se calcolare l'intercetta per questo modello. Se impostato su
        False, nei calcoli non verrà usata nessuna intercetta
        (e.g. i dati dovrebbero essere già centrati).

    Attributes
    ----------
    coef_ : array, shape (n_features, ) o (n_targets, n_features)
        Coefficienti stimati per il problema di regressione lineare.
        Se durate il fit sono passati più target (y 2D), questo è un
        array 2D di forma (n_targets, n_features), mentre se viene
        passato solo un target, questo è un array 1D di lunghezza
        n_features.

    intercept_ : array
        Termine costante nel modello lineare.
    """
    def __init__(self, fit_intercept=True):
        self.fit_intercept = fit_intercept

    def fit(self, X, y):
        if self.fit_intercept:
            X = np.c_[np.ones(len(X)), X]

        # TODO: stimare i coefficienti con il metodo dei minimi quadrati
        self.coef_ = None
        raise NotImplementedError

        if self.fit_intercept:
            self.intercept_ = self.coef_[0]
            self.coef_ = self.coef_[1:]
        else:
            self.intercept_ = 0

        return self

    def predict(self, X):
        return self.intercept_ + np.dot(X, self.coef_)
