from sklearn.base import TransformerMixin
from sklearn.utils.validation import check_is_fitted


class RiempireNAMedia(TransformerMixin):
    """Riempie i valori mancanti utilizzando la media.

    Attributes
    ----------
    media_dict_ : dict
        Dizionario che associa ad ogni colonna il suo valore medio.

    """
    def __init__(self):
        pass

    def fit(self, X, y=None):
        self.media_dict_ = X.mean().to_dict()

        return self

    def transform(self, X, y=None):
        check_is_fitted(self, "media_dict_")

        return X.fillna(self.media_dict_)


class RiempireNAItemWeight(TransformerMixin):
    """Riempie i valori mancanti di 'Item_Weight'.

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
    """Riempie i valori mancanti di 'Outlet_Size'.
    """
    def __init__(self):
        pass

    def fit(self, X, y=None):

        return self

    def transform(self, X, y=None):
        is_null = X["Outlet_Size"].isnull()
        is_tier2 = X["Outlet_Location_Type"] == "Tier 2"
        is_grocery = X["Outlet_Type"] == "Grocery Store"
        is_type2 = X["Outlet_Type"] == "Supermarket Type2"
        is_type3 = X["Outlet_Type"] == "Supermarket Type3"
        X.loc[is_null & (is_tier2 | is_grocery), "Outlet_Size"] = "Small"
        X.loc[is_null & (is_tier2 | is_grocery), "Outlet_Size"] = "Small"
        X.loc[is_null & is_type2, "Outlet_Size"] = "Medium"
        X.loc[is_null & is_type3, "Outlet_Size"] = "Medium"

        return X
