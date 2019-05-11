import math
import numpy as np
from sklearn.metrics import mean_squared_error


def radice_errore_quadratico_medio(y_true, y_pred, sample_weight=None,
        multioutput="uniform_average"):
    """Radice dell'errore quadratico medio

    Parameters
    ----------
    y_true : array-like of shape = (n_samples) or (n_samples, n_outputs)
        Ground truth (correct) target values.
    y_pred : array-like of shape = (n_samples) or (n_samples, n_outputs)
        Estimated target values.
    sample_weight : array-like of shape = (n_samples), optional
        Sample weights.
    multioutput : string in ['raw_values', 'uniform_average']
        or array-like of shape (n_outputs)
        Defines aggregating of multiple output values.
        Array-like value defines weights used to average errors.
        'raw_values' :
            Returns a full set of errors in case of multioutput input.
        'uniform_average' :
            Errors of all outputs are averaged with uniform weight.
    Returns
    -------
    loss : float or ndarray of floats
        A non-negative floating point value (the best value is 0.0), or an
        array of floating point values, one for each individual target.
    """
    return np.sqrt(mean_squared_error(y_true, y_pred,
        sample_weight=sample_weight, multioutput=multioutput))


def criterio_informazione_akaike(stimatore, X, y, distribuzione="normale"):
    """Criterio d'informazione di Akaike"""
    n, k = X.shape
    k += 2 # intercetta e deviazione standard
    y_pred = stimatore.predict(X)
    rss = sum((y - y_pred) ** 2)
    var_hat = rss / n

    if distribuzione == "normale":
        logl = (-math.log(2 * math.pi) * n / 2 - math.log(var_hat) * n / 2 -
            rss / (2 * var_hat))
    else:
        ValueError("La distribuzione {} non è attualmente supportata.".format(
            distribuzione))

    return 2 * k - 2 * logl


class MetricheClassificazione:
    @staticmethod
    def n_negativi(y_true, y_pred):
        n = (y_true == 0).sum()

        return n

    @staticmethod
    def n_positivi(y_true, y_pred):
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        p = None
        # ============================================

        return p

    @staticmethod
    def n_previsti_negativi(y_true, y_pred):
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        pn = None
        # ============================================

        return pn

    @staticmethod
    def n_previsti_positivi(y_true, y_pred):
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        pp = None
        # ============================================

        return pp

    @staticmethod
    def n_veri_negativi(y_true, y_pred):
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        vn = None
        # ============================================

        return vn

    @staticmethod
    def n_falsi_positivi(y_true, y_pred):
        fp = ((y_true != y_pred) & (y_pred == 1)).sum()

        return fp

    @staticmethod
    def n_falsi_negativi(y_true, y_pred):
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        fn = None
        # ============================================

        return fn

    @staticmethod
    def n_veri_positivi(y_true, y_pred):
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        vp = None
        # ============================================

        return vp

    @staticmethod
    def tasso_falsi_positivi(y_true, y_pred):
        fp = MetricheClassificazione.n_falsi_positivi(y_true, y_pred)
        n = MetricheClassificazione.n_negativi(y_true, y_pred)
        tfp = fp / n

        return tfp

    @staticmethod
    def tasso_veri_positivi(y_true, y_pred):
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        tvp = None
        # ============================================

        return tvp

    @staticmethod
    def precisione(y_true, y_pred):
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        pr = None
        # ============================================

        return pr

    @staticmethod
    def richiamo(y_true, y_pred):
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        rc = None
        # ============================================

        return rc

    @staticmethod
    def punteggio_f1(y_true, y_pred):
        # ============== YOUR CODE HERE ==============
        raise NotImplementedError
        f1 = None
        # ============================================

        return f1
