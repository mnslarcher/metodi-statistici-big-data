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


def gauss_aic(stimatore, X, y):
    """Criterio d'informazione di Akaike, caso gaussiano"""
    n, k = X.shape
    k += 2 # intercetta e deviazione standard
    y_pred = stimatore.predict(X)
    rss = sum((y - y_pred) ** 2)
    var_hat = rss / n
    logl = (-math.log(2 * math.pi) * n / 2 - math.log(var_hat) * n / 2 - rss /
        (2 * var_hat))

    return 2 * k - 2 * logl
