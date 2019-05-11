from .. metriche import MetricheClassificazione
import numpy as np
import pytest

y_true = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
y_pred = np.array([0, 0, 0, 1, 0, 0, 1, 1, 1, 1])


def test_n_negativi():
    n = MetricheClassificazione.n_negativi(y_true, y_pred)

    assert n == 4

def test_n_positivi():
    p = MetricheClassificazione.n_positivi(y_true, y_pred)

    assert p == 6

def test_n_previsti_negativi():
    pn = MetricheClassificazione.n_previsti_negativi(y_true, y_pred)

    assert pn == 5

def test_n_previsti_positivi():
    pp = MetricheClassificazione.n_previsti_positivi(y_true, y_pred)

    assert pp == 5

def test_n_veri_negativi():
    vn = MetricheClassificazione.n_veri_negativi(y_true, y_pred)

    assert vn == 3

def test_n_falsi_positivi():
    fp = MetricheClassificazione.n_falsi_positivi(y_true, y_pred)

    assert fp == 1

def test_n_falsi_negativi():
    fn = MetricheClassificazione.n_falsi_negativi(y_true, y_pred)

    assert fn == 2

def test_n_veri_positivi():
    vp = MetricheClassificazione.n_veri_positivi(y_true, y_pred)

    assert vp == 4

def test_tasso_falsi_positivi():
    tfp = MetricheClassificazione.tasso_falsi_positivi(y_true, y_pred)

    assert tfp == pytest.approx(1 / 4)

def test_tasso_veri_positivi():
    tvp = MetricheClassificazione.tasso_veri_positivi(y_true, y_pred)

    assert tvp == pytest.approx(4 / 6)

def test_precisione():
    pr = MetricheClassificazione.precisione(y_true, y_pred)

    assert pr == pytest.approx(4 / 5)

def test_richiamo():
    rc = MetricheClassificazione.richiamo(y_true, y_pred)

    assert rc == pytest.approx(4 / 6)

def test_punteggio_f1():
    f1 = MetricheClassificazione.punteggio_f1(y_true, y_pred)
    pr = 4 / 5
    rc = 4 / 6

    assert f1 == 2 * (pr * rc) / (pr + rc)
