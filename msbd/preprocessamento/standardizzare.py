from sklearn.base import TransformerMixin
from sklearn.utils.validation import check_is_fitted


class Standardizzare(TransformerMixin):
    """Standardizza i dati rimuovendo la media e dividendo per la
    deviazione standard

    Parameters
    ----------
    con_media : ...

    con_dev_std : ...

    Attributes
    ----------
    media_ : ...

    dev_std_ : ...
    """
    def __init__(self, con_media=True, con_dev_std=True):
        self.con_media = con_media
        self.con_dev_std = con_dev_std

    def fit(self, X, y=None):
        if self.con_media:
            self.media_ = X.mean()
        else:
            self.media_ = None

        if self.con_dev_std:
            self.dev_std_ = X.std()
        else:
            self.dev_std_ = None

        return self

    def transform(self, X):
        check_is_fitted(self, ["media_", "dev_std_"])

        if self.con_media:
            X -= self.media_

        if self.con_dev_std:
            X /= self.dev_std_

        return X

    def inverse_transform(self, X):
        check_is_fitted(self, ["media_", "dev_std_"])

        # TODO: applicare a X la trasformazione inversa
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        # ============================================

        return X
