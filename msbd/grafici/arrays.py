import matplotlib.pyplot as plt


def grafico_due_vettori(a, b, figsize=(4, 4)):
    """Grafico dei vettori a e b.

    Parameters
    ----------
    a : array, shape (n, )
        Vettore a.

    b : array, shape (n, )
        Vettore b.

    figsize : tuple, optional, default (4, 4)
        Dimensioni del grafico.
    """
    plt.figure(figsize=figsize)
    plt.title("Grafico dei vettori $a$ e $b$")
    vettore_a = plt.arrow(0, 0, a[0], a[1], head_width=0.05, head_length=0.05,
        color="b")
    vettore_b = plt.arrow(0, 0, b[0], b[1], head_width=0.05, head_length=0.05,
        color="r")
    plt.legend(
        [vettore_a, vettore_b],
        ["$a$: [{:.2f}, {:.2f}]".format(*a),
         "$b$: [{:.2f}, {:.2f}]".format(*b)],
        loc="lower right"
    )
    plt.xlabel("x")
    plt.ylabel("y")
