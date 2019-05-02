from itertools import product
from sklearn.metrics import auc
from sklearn.metrics import average_precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt


def grafico_curva_precisione_richiamo(y_true, y_score,
        titolo="Curva precisione-richiamo"):
    plt.title(titolo)
    precisione, richiamo, _ = precision_recall_curve(y_true, y_score)
    plt.plot(richiamo, precisione, lw=2, label="Classificatore (AP = {:.2f})".\
        format(average_precision_score(y_true, y_score)))
    baseline = y_true.mean()
    plt.plot([0, 1], [baseline, baseline], lw=2, ls="--",
        label="Baseline (AP = {:.2f})".format(baseline))
    plt.xlabel("Richiamo")
    plt.ylabel("Precisione")
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.grid()
    plt.legend()


def grafico_curva_roc(y_true, y_score, titolo="Curva ROC"):
    plt.title(titolo)
    tfp, tvp, _ = roc_curve(y_true, y_score)
    plt.plot(tfp, tvp, lw=2, label="Classificatore (AUC = {:.2f})".format(
        auc(tfp, tvp)))
    plt.plot([0, 1], [0, 1], lw=2, ls="--", label="Baseline (AUC = 0.5)")
    plt.xlabel("Tasso falsi positivi")
    plt.ylabel("Tasso veri positivi (richiamo)")
    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.grid()
    plt.legend()


def grafico_matrice_confusione(y_true, y_pred, classi,
        titolo="Matrice di confusione", cmap=plt.cm.Blues):
    plt.title(titolo)
    cm = confusion_matrix(y_true, y_pred)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar(fraction=0.04, pad=0.2)
    tick_marks = range(len(classi))
    plt.xticks(tick_marks, classi, rotation=90)
    plt.yticks(tick_marks, classi)
    thresh = cm.max() / 2
    for i, j in product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], 'd'), horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")
    plt.ylabel("Classe osservata")
    plt.xlabel("Classe prevista")
