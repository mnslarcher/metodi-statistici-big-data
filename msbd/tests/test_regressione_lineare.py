from .. modello_lineare import RegressioneLineare
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import numpy as np


X, y = make_regression(n_samples=100, n_features=10, bias=5, random_state=42)

rl_fit_intercept_true = RegressioneLineare(fit_intercept=True)
lr_fit_intercept_true = LinearRegression(fit_intercept=True)

rl_fit_intercept_true.fit(X, y)
lr_fit_intercept_true.fit(X, y)

rl_fit_intercept_false = RegressioneLineare(fit_intercept=False)
lr_fit_intercept_false = LinearRegression(fit_intercept=False)

rl_fit_intercept_false.fit(X, y)
lr_fit_intercept_false.fit(X, y)


def test_regressione_lineare_fit_intercept_true_intercept_():
    assert np.allclose(rl_fit_intercept_true.intercept_,
        lr_fit_intercept_true.intercept_)


def test_regressione_lineare_fit_intercept_true_coef_():
    assert np.allclose(rl_fit_intercept_true.coef_,
        lr_fit_intercept_true.coef_)


def test_regressione_lineare_fit_intercept_false_intercept_():
    assert np.allclose(rl_fit_intercept_false.intercept_,
        lr_fit_intercept_false.intercept_)


def test_regressione_lineare_fit_intercept_false_coef_():
    assert np.allclose(rl_fit_intercept_false.coef_,
        lr_fit_intercept_false.coef_)
