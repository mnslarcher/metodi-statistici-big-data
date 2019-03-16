from sklearn.base import TransformerMixin


class Sostituire(TransformerMixin):
    """Sostituisce i valori di un DataFrame in base a un dizionario

    Parameters
    ----------
    to_replace : dict
        Dizionario innestato, es., {"a": {"b": "c"}}, si legge come:
        cerca nella colonna "a" il valore "b" e sostituiscilo con "c".
    """
    def __init__(self, to_replace):
        self.to_replace = to_replace

    def fit(self, X, y=None):

        return self

    def transform(self, X):
        X.replace(self.to_replace, inplace=True)

        return X
