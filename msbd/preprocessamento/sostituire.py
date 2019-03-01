from sklearn.base import TransformerMixin
from sklearn.utils.validation import check_is_fitted


class Sostituire(TransformerMixin):
    """Sostituisce i valori mancanti di un DataFrame.

    Parameters
    ----------
    to_replace : dict
        Dizionario innestato, es., {'a': {'b': 'c'}}, si legge come:
        cerca nella colonna 'a' il valore 'b' e sostituiscilo con 'c'.
    """
    def __init__(self, to_replace):
        self.to_replace = to_replace

    def fit(self, X, y=None):

        return self

    def transform(self, X, y=None):
        X.replace(self.to_replace, inplace=True)

        return X
