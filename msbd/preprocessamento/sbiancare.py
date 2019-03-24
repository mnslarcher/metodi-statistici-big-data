from sklearn.base import TransformerMixin
from sklearn.utils.validation import check_is_fitted
import numpy as np


class Sbiancare(TransformerMixin):
    """Trasforma i dati rendendoli a media zero e varianza unitaria"""

    def __init(self):
        pass

    def fit(self, X, y=None):
        self.media_ = X.mean(axis=0)
        sigma = np.cov(X.T)

        # decomposizione in autovettori (EVD)
        self.d_, self.E_ = np.linalg.eig(sigma)

        return self

    def transform(self, X):
        check_is_fitted(self, ["media_", "d_", "E_"])

        X -= self.media_

        return X.dot(self.E_).dot(np.diag(1 / np.sqrt(self.d_))).dot(self.E_.T)

    def inverse_transform(self, X):
        check_is_fitted(self, ["media_", "d_", "E_"])

        # TODO: applicare a X la trasformazione inversa
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        # ============================================

        return X