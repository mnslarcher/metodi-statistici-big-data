from sklearn.base import TransformerMixin
from sklearn.utils.validation import check_is_fitted


class RiempireNAMedia(TransformerMixin):
    """Riempie i valori mancanti utilizzando la media

    Attributes
    ----------
    media_dict_ : dict
        Dizionario che associa ad ogni colonna il suo valore medio.

    """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        # DataFrame.mean() ha come default numeric_only=True
        self.media_dict_ = X.mean().to_dict()

        return self

    def transform(self, X, y=None):
        check_is_fitted(self, "media_dict_")

        return X.fillna(self.media_dict_)


class RiempireNAItemWeight(TransformerMixin):
    """Riempie i valori mancanti di 'Item_Weight'

    Attributes
    ----------
    weight_dict_ : dict
        Dizionario che associa ad ogni 'Item_Identifier' il suo
        'Item_Weight' medio.

    """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        self.weight_dict_ = X[["Item_Identifier", "Item_Weight"]].groupby(
            "Item_Identifier").mean()["Item_Weight"].to_dict()

        return self

    def transform(self, X, y=None):
        check_is_fitted(self, "weight_dict_")

        value = {idx : self.weight_dict_.get(identifier) for idx, identifier in
            zip(X.index, X["Item_Identifier"])}

        X["Item_Weight"].fillna(value, inplace=True)

        return X


class RiempireNAOutletSize(TransformerMixin):
    """Riempie i valori mancanti di 'Outlet_Size'"""
    def __init__(self):
        pass

    def fit(self, X, y=None):

        return self

    def transform(self, X, y=None):
        # TODO: definire una trasformazione opportuna sulla base di
        #       quanto scoperto tramite l'analisi esplorativa
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        # ============================================

        return X
