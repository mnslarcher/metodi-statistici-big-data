import pandas as pd


def grafico_importanza_variabili(importanze, variabili, max_num=None,
        titolo="Importanza delle variabili"):
    importanze = pd.Series(importanze, index=variabili).sort_values(
        ascending=False)
    importanze[:max_num].plot(kind="bar", grid=True, title=titolo,
        color="tab:blue")
