from sklearn.base import TransformerMixin
from sklearn.utils.validation import check_is_fitted


class Eliminare(TransformerMixin):
    """Elimina le colonne specificate da un DataFrame

    Parameters
    ----------
    columns : singola string o list-like
        Colonne da eliminare.
    """
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):

        return self

    def transform(self, X, y=None):

        return X.drop(columns=self.columns)
