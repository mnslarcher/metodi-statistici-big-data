from sklearn import datasets
import matplotlib.pyplot as plt


def grafico_progressione_diabete_vs_bmi(x, y):
    """Grafico della progressione del diabete al variare del BMI"""
    plt.title("Progressione del diabete vs BMI")
    plt.scatter(x, y, alpha=.75)
    plt.xlabel("BMI")
    plt.ylabel("Progressione del diabete")
