import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


CANALI = ["R", "G", "B", "A"]
CLASSI = [
    "red soil",
    "cotton crop",
    "grey soil",
    "damp grey soil",
    "soil with vegetation stubble",
    "very damp grey soil",
]
NUMERO_CLASSE = dict(zip([1, 2, 3, 4, 5, 7], CLASSI))


def grafico_immagine_satellitare(X, y):
    plt.suptitle("Un'immagine per classe selezionata casualmente")

    for i, (num_cl, cl) in enumerate(NUMERO_CLASSE.items()):
        plt.subplot(231 + i)
        plt.title(cl)
        idx = np.random.choice(X.loc[y == num_cl].index)
        image = X.loc[idx].values.reshape((3, 3, 4)).astype(np.uint8)
        plt.imshow(image, interpolation='none')
        plt.xticks([0.5, 1.5], [])
        plt.yticks([0.5, 1.5], [])
        plt.grid(color='black')


def diagrammi_scatola_baffi_classi(x, y):
    sns.boxplot(x=np.asarray(x), y=np.asarray(y))
    plt.xticks(range(6), CLASSI, rotation="vertical", fontsize=10)


def diagrammi_scatola_baffi_pixel(X, y, posizione):
    plt.suptitle("Diagramma a scatola e baffi dei pixel in posizione "
        "{} per ogni combinazione di classe e canale".format(posizione))

    for i in range(4):
        plt.subplot(221 + i)
        canale = CANALI[i]
        plt.title('Canale {}'.format(canale))
        diagrammi_scatola_baffi_classi(y,
            X["Pixel{}_{}".format(posizione, canale)])
        plt.xlabel("")

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)


def grafico_componenti(X, y):
    for i, classe in NUMERO_CLASSE.items():
        plt.scatter(X[y == i, 0], X[y == i, 1], color=plt.cm.Set2(i),
            alpha=0.5, label=classe)
    plt.legend()
    plt.xlabel("Prima componente")
    plt.ylabel("Seconda componente")
    plt.xticks([])
    plt.yticks([])
