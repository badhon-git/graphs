# em wave from maxwell's equation

import numpy as np
import matplotlib.pyplot as plt

N = 200                      
mu, eps = 1.0, 1.0           
dx, dt = 1.0, 0.5           

x = np.arange(N)
E = np.exp(-((x - 100) / 8) ** 2)    
H = np.zeros(N)                      

plt.ion()
fig, ax = plt.subplots()
lineE, = ax.plot(x, E, label="E")
lineH, = ax.plot(x, H, label="H")
ax.set_ylim(-1, 1)
ax.legend()

for n in range(1000):
    # Faraday
    H[:-1] += dt / (mu * dx) * (E[1:] - E[:-1])
    # Ampere
    E[1:] += dt / (eps * dx) * (H[1:] - H[:-1])

    if n % 2 == 0:
        lineE.set_ydata(E)
        lineH.set_ydata(H)
        ax.set_title(f"step {n}")
        plt.pause(0.01)
