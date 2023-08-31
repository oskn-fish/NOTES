import matplotlib.pyplot as plt
import numpy as np
import os

MESH = 1000
KERNELS = 10
SIGMA = 0.1
X_MIN  = -1
X_MAX = 1
MU_MAX = 0.5
MU_MIN = -0.5

x = np.linspace(X_MIN, X_MAX, MESH)
mus = np.linspace(MU_MIN, MU_MAX, KERNELS)
sigmas = np.full(KERNELS, SIGMA)

def pdf(x: np.ndarray, mu, sigma):
    return np.exp(-(x-mu)**2/(2*sigma**2)) # 形が大切であって，定数倍はweightで吸収できるので無視して良い

for mu, sigma in zip(mus, sigmas):
    plt.plot(x, pdf(x, mu, sigma))

pic_path = os.path.join(os.path.dirname(__file__), "gauss_kernel.png")
plt.savefig(pic_path)
plt.show()
