#%%
import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D

MESH = 100 # 1000にするとメモリを12GB以上消費してしまう．まさに次元の呪い
KERNELS = 10**2
SIGMA = 0.1
X_MIN  = -1
X_MAX = 1
MU_MAX = 0.5
MU_MIN = -0.5

mesh = np.linspace(X_MIN, X_MAX, MESH)
mus = np.linspace(MU_MIN, MU_MAX, KERNELS)
sigmas = np.full(KERNELS, SIGMA)

# def pdf(x: np.ndarray, mu, sigma):
#     return np.exp(-(x-mu)**2/(2*sigma**2)) # 形が大切であって，定数倍はweightで吸収できるので無視して良い

def pdf(x, y, mu, sigma):
    sigma_array = np.identity(2)*sigma
    x_y = np.vstack([x,y])
    return np.exp(-(x_y-mu).T@np.linalg.inv(sigma_array)@(x_y-mu)/2) # 定数倍はweightで調節されるので木にしなくて良い．

x, y = np.mgrid[X_MIN:X_MAX:complex(0,MESH), X_MIN:X_MAX:complex(0,MESH)]
x, y = x.flatten(), y.flatten()
#%%
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

for mu, sigma in zip(mus, sigmas):
    ax.plot_surface(x, y, pdf(x, y, mu, sigma), cmap="winter")
    # print(x)
    # print(y)
    # print(pdf(x,y, mu, sigma))
    # print("")

pic_path = os.path.join(os.path.dirname(__file__), "gauss_kernel_3d.png")
plt.savefig(pic_path)
plt.show()