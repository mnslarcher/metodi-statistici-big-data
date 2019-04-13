import pandas as pd


def grafico_importanza_variabili(importanze, variabili, max_num=None):
        importanze = pd.Series(importanze, index=variabili).sort_values(
            ascending=False)
        importanze[:max_num].plot(kind="bar", grid=True,
            title="Importanza delle variabili", color="tab:blue")
