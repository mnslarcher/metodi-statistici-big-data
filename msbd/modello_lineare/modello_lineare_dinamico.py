import numpy as np


class ModelloLineareDinamico:
    """Modello lineare dinamico.

    Parameters
    ----------
    x0_hat : array, shape (n_x, 1)
        Stima del vettore di stato iniziale.

    P0_hat : array, shape (n_x, n_x)
        Stima della matrice di covarianza del vettore di stato iniziale.

    Attributes
    ----------
    x_hat_ : list
        Lista dei vettori di stato stimati.

    P_hat_ : list
        Lista delle matrici di covarianza dei vettori di stato stimate.
    """
    def __init__(self, x0_hat, P0_hat):
        self.x_hat_ = [x0_hat]
        self.P_hat_ = [P0_hat]

    @staticmethod
    def eq1(F, x, G, u, w=0):
        """Prima equazione del modello lineare dinamico.

        Parameters
        ----------
        F : array, shape (n_x, n_x)
            Matrice del sistema - stato al tempo k - 1.

        x : array, shape (n_x, 1)
            Vettore di stato al tempo k - 1.

        G : array, shape (n_x, n_u)
            Matrice del sistema - input al tempo k - 1.

        u : array, shape (n_u, 1)
            Vettore di input al tempo k - 1.

        w : array, shape (n_x, 1), optional, default 0
            Vettore del rumore del processo al tempo k.

        Returns
        -------
        x : array, shape (n_x, 1)
            Vettore di stato al tempo k.
        """
        # TODO: completare il metodo
        # ============== YOUR CODE HERE ==============
        x = None # x = Fx + Gu + w
        raise NotImplementedError
        # ============================================

        return x

    @staticmethod
    def eq2(H, x, v=0):
        """Seconda equazione del modello lineare dinamico.

        Parameters
        ----------
        H : array, shape (n_y, n_x)
            Matrice delle osservazioni al tempo k.

        x : array, shape (n_x, 1)
            Vettore di stato al tempo k.

        v : array, shape (n_y, 1), optional, default 0
            Vettore del rumore di misurazione al tempo k.

        Returns
        -------
        y : array, shape (n_y, 1)
            Vettore di output al tempo k.
        """
        # TODO: completare il metodo
        # ============== YOUR CODE HERE ==============
        y = None # y = Hx + v
        raise NotImplementedError
        # ============================================

        return y

    def partial_fit(self, F, G, u, H, Q, R, z):
        """Filtro di Kalman.

        Parameters
        ----------
        F : array, shape (n_x, n_x)
            Matrice del sistema - stato al tempo k - 1.

        G : array, shape (n_x, n_u)
            Matrice del sistema - input al tempo k - 1.

        u : array, shape (n_u, 1)
            Vettore di input al tempo k - 1.

        H : array, shape (n_y, n_x)
            Matrice delle osservazioni al tempo k.

        Q : array, shape (n_x, n_x)
            Matrice di covarianza dell'errore del processo w
            al tempo k - 1.

        R : array, shape (n_y, n_y)
            Matrice di covarianza del vettore di output y al tempo k.

        z : array, shape (n_y, 1)
            Misurazione di y al tempo k.
        """
        # TODO: completare il metodo
        # ============== YOUR CODE HERE ==============
        x_hat = None # 1.
        P_hat = None # 2.
        K = None # 3.
        x_hat = None # 4.
        P_hat = None # 5.
        raise NotImplementedError
        # ============================================
        self.x_hat_.append(x_hat)
        self.P_hat_.append(P_hat)

        return self
