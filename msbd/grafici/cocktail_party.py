import matplotlib.pyplot as plt


def grafico_cocktail_party(t, S, X, S_hat=None):
    """Grafico del problema del cocktail party"""
    plt.suptitle("Problema del cocktail party")

    plt.subplot(411 + 200 * (S_hat is not None))
    plt.plot(t, S[:, 0])
    plt.ylabel("$s_1(t)$")

    plt.subplot(412 + 200 * (S_hat is not None))
    plt.plot(t, S[:, 1])
    plt.ylabel("$s_2(t)$")

    plt.subplot(413 + 200 * (S_hat is not None))
    plt.plot(t, X[:, 0], color="tab:orange")
    plt.ylabel("$x_1(t)$")

    plt.subplot(414 + 200 * (S_hat is not None))
    plt.plot(t, X[:, 1], color="tab:orange")
    plt.ylabel("$x_2(t)$")

    if S_hat is not None:
        plt.subplot(615)
        plt.plot(t, S_hat[:, 0], color="tab:green")
        plt.ylabel("$\hat{s}t)$")

        plt.subplot(616)
        plt.plot(t, S_hat[:, 1], color="tab:green")
        plt.ylabel("$\hat{s}(t)$")

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
