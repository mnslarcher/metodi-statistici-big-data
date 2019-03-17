from ..grafici import grafico_coefficienti
from ..metriche import radice_errore_quadratico_medio
import matplotlib.pyplot as plt
import pandas as pd


def esperimento_regolarizzazione(stimatore, alpha_list, X_train, y_train,
        X_val, y_val):
    variabili = X_train.columns
    esperimento = pd.DataFrame(columns=variabili)
    r2_train_list = []
    r2_val_list = []
    rmse_train_list = []
    rmse_val_list = []

    for alpha in alpha_list:
        stimatore.set_params(alpha=alpha)
        stimatore.fit(X_train, y_train)
        esperimento = esperimento.append(pd.DataFrame([stimatore.coef_],
            columns=variabili))

        plt.figure(figsize=(15, 3))

        print("\n" + "-" * 79)
        print("Alpha: {} |".format(alpha))
        print("-" * len(str("Alpha: {} -".format(alpha))) + "\n")

        print("Intercetta: {:.2f}".format(stimatore.intercept_))
        grafico_coefficienti(
            stimatore.coef_,
            variabili
        )

        plt.show()

        r2_train = stimatore.score(X_train, y_train)
        r2_val = stimatore.score(X_val, y_val)
        rmse_train = radice_errore_quadratico_medio(y_train,
            stimatore.predict(X_train))
        rmse_val = radice_errore_quadratico_medio(y_val,
            stimatore.predict(X_val))

        r2_train_list.append(r2_train)
        r2_val_list.append(r2_val)
        rmse_train_list.append(rmse_train)
        rmse_val_list.append(rmse_val)

        print("R2 training: {:.4f}".format(r2_train))
        print("R2 validation: {:.4f}".format(r2_val))
        print("RMSE training: {:.4f}".format(rmse_train))
        print("RMSE validation: {:.4f}".format(rmse_val))

    esperimento["Alpha"] = [str(alpha) for alpha in alpha_list]
    esperimento["R2_Train"] = r2_train_list
    esperimento["R2_Val"] = r2_val_list
    esperimento["RMSE_Train"] = rmse_train_list
    esperimento["RMSE_Val"] = rmse_val_list

    esperimento.set_index('Alpha', inplace=True)

    return esperimento
