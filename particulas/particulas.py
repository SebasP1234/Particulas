import matplotlib.pyplot as plt
import numpy as np
class particulas():
    def __init__(self, masa, x_i, y_i, v, alpha, a, beta, r):
        self.masa = masa
        self.r = r
        self.x_i = x_i
        self.y_i = y_i
        self.v = v
        self.alpha = alpha
        self.V = v * np.array([np.cos(alpha), np.sin(alpha)])
        self.V[np.abs(self.V) < 1e-10] = 0.0
        self.a = a
        self.beta = beta
        self.A = a * np.array([np.cos(beta), np.sin(beta)])
        self.A[np.abs(self.A) < 1e-10] = 0.0
        self.R_i = np.array([[x_i],
                              [y_i]])
