import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.base import clone
from sklearn.base import RegressorMixin
from sklearn.utils.validation import check_is_fitted


class Stepwise(BaseEstimator, RegressorMixin):
    """Regressione stepwise

    Parameters
    ----------
    stimatore : ...

    criterio : ...

    procedura : ...

    verboso : ...

    Attributes
    ----------
    variabili_selezionate_ : ...

    valore_criterio_ : ...

    """
    def __init__(self, stimatore, criterio, procedura,
            verboso=False):
        self.stimatore = stimatore
        self.criterio = criterio
        self.procedura = procedura
        self.verboso = verboso

    def _passo_avanti(self, X, y):
        valore_criterio = float('inf')

        for var in self._variabili_non_incluse:
            nuovo_stimatore = clone(self.stimatore)
            variabili_selezionate = self.variabili_selezionate_ + [var]

            nuovo_stimatore.fit(X[variabili_selezionate], y)

            nuovo_valore_criterio = self.criterio(nuovo_stimatore,
                X[variabili_selezionate], y)
            if nuovo_valore_criterio < valore_criterio:
                valore_criterio = nuovo_valore_criterio
                variabile_selezionata = var
                stimatore = nuovo_stimatore
        return valore_criterio, variabile_selezionata, stimatore

    def _passo_indietro(self, X, y):
        # TODO: implementare il passo indietro
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        # ============== YOUR CODE HERE ==============

    def _selezione_avanti(self, X, y):
        self.variabili_selezionate_ = []
        self._variabili_non_incluse = X.columns.tolist()

        while len(self._variabili_non_incluse) > 0:
            if self.verboso:
                print("[INFO] valore criterio: {:.4f}".format(
                    self.valore_criterio_))
                print("[INFO] numero variabili selezionate: {}".format(
                    len(self.variabili_selezionate_)))
                print("[INFO] variabili selezionate: {}\n".format(", ".join(
                    self.variabili_selezionate_)))

            valore_criterio, variabile_selezionata, stimatore = \
                self._passo_avanti(X, y)

            if valore_criterio < self.valore_criterio_:
                self.valore_criterio_ = valore_criterio
                self.variabili_selezionate_.append(variabile_selezionata)
                self._variabili_non_incluse.remove(variabile_selezionata)
                self.stimatore_ = stimatore
            else:
                break

    def _selezione_indietro(self, X, y):
        # TODO: implementare la selezione all'indietro
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        # ============== YOUR CODE HERE ==============

    def _selezione_ibrida(self, X, y):
        # TODO: implementare la selezione ibrida
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        # ============== YOUR CODE HERE ==============

    def fit(self, X, y):
        self.stimatore_ = clone(self.stimatore)
        self.valore_criterio_ = float('inf')

        if self.procedura == 'avanti':
            self._selezione_avanti(X, y)
        elif self.procedura == 'indietro':
            self._selezione_indietro(X, y)
        elif self.procedura == 'ibrida':
            self._selezione_ibrida(X, y)
        else:
            raise ValueError("{} non è una procedura valida.".format(
                self.procedura))

    def predict(self, X):
        check_is_fitted(self, ["stimatore_", "variabili_selezionate_"])
        return self.stimatore_.predict(X[self.variabili_selezionate_])
