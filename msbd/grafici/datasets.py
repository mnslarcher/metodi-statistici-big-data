from sklearn import datasets
import matplotlib.pyplot as plt


def grafico_progressione_diabete_vs_bmi(return_X_y=False):
    """Grafico della progressione del diabete al variare del BMI.

    Vedere https://scikit-learn.org/stable/datasets/index.html#diabetes-dataset
    """
    X, y = datasets.load_diabetes(return_X_y=True)
    X = X[:, [2]] # tengo solo la variabile Body mass index

    plt.title("Progressione del diabete vs BMI")
    plt.scatter(X, y)
    plt.xlabel("BMI")
    plt.ylabel("Progressione del diabete")

    if return_X_y:
        return X, y
