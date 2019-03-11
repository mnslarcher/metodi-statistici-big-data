from sklearn.base import TransformerMixin
from sklearn.utils.validation import check_is_fitted
import pandas as pd


class OttenereDummy(TransformerMixin):
    """Trasforma le variabili con dtype 'object' or 'category' in dummy

    Parameters
    ----------
    drop_first : bool, default False
        Se ottenere k-1 dummy da k livelli categoriali attraverso la
        rimozione del primo livello.

    Attributes
    ----------
    columns_ : Index
        Colonne del DataFrame a seguito della trasformazione.

    """
    def __init__(self, drop_first=False):
        self.drop_first = drop_first

    def fit(self, X, y=None):
        # TODO: ottenere self.columns_ senza utilizzare get_dummies()
        # ============== YOUR CODE HERE ==============
        self.columns_ = pd.get_dummies(X, drop_first=self.drop_first).columns
        # ============================================

        return self

    def transform(self, X, y=None):
        check_is_fitted(self, "columns_")

        X = pd.get_dummies(X)
        X = X.reindex(columns=self.columns_, fill_value=0)

        return X.astype(float)
