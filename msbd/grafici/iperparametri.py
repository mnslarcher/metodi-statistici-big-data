import matplotlib.pyplot as plt


def grafico_metrica_iperparametro(risultati, iperparam, metrica, alpha=0.75,
        s=300):
    plt.title("{} al variare di {}".format(metrica, iperparam))
    plt.scatter(risultati[iperparam], risultati[metrica], s=s, alpha=alpha)
    plt.xlabel(iperparam)
    plt.ylabel(metrica)
    plt.grid()


def grafico_metrica_iperparametri(risultati, iperparam1, iperparam2, metrica,
        alpha=0.75, s=300):
    plt.title("{} al variare di {} e {}".format(metrica, iperparam1,
        iperparam2))
    plt.scatter(risultati[iperparam1], risultati[iperparam2],
        c=risultati[metrica], cmap=plt.cm.RdBu_r, alpha=alpha, s=s)
    plt.colorbar()
    plt.xlabel(iperparam1)
    plt.ylabel(iperparam2)
    plt.grid()
