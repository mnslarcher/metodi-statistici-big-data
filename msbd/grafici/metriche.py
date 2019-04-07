from itertools import product
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def grafico_matrice_confusione(y_true, y_pred, classi,
    titolo="Matrice di confusione", cmap=plt.cm.Blues):
    cm = confusion_matrix(y_true, y_pred)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(titolo)
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
