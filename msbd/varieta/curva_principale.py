import numpy as np
from scipy.interpolate import UnivariateSpline
from scipy.optimize import minimize


class CurvaPrincipale:
    def _distanza_euclidea(self, l, X):
        X_prz = np.array((self.f1_hat(l), self.f2_hat(l))).T
        return ((X - X_prz) ** 2).sum()

    def partial_fit(self, X):
        if not hasattr(self, "l_hat"):
            U, s, Vt = np.linalg.svd(X, full_matrices=False)
            V = Vt.T
            V1 = V[:, [0]]
            H1 = V1.dot(V1.T)
            def f1_hat(l): return V1[0, 0] * l
            def f2_hat(l): return V1[1, 0] * l

            self.X_prz = X.dot(H1)
            self.l_hat = U[:, 0] * s[0]
            self.f1_hat = f1_hat
            self.f2_hat = f2_hat
        else:
            l_hat_argsort = np.argsort(self.l_hat)
            self.f1_hat = UnivariateSpline(x=self.l_hat[l_hat_argsort],
                y=X[l_hat_argsort, 0])
            self.f2_hat = UnivariateSpline(x=self.l_hat[l_hat_argsort],
                y=X[l_hat_argsort, 1])

            self.l_hat = minimize(lambda l: self._distanza_euclidea(l, X),
                self.l_hat).x
            self.X_prz = np.c_[self.f1_hat(self.l_hat),
                self.f2_hat(self.l_hat)]

        return self
