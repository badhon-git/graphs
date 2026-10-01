import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 5000)

cases = [
    (1, 1, np.pi / 2),   
    (1, 2, np.pi / 2),   
    (3, 2, np.pi / 2),
    (3, 4, np.pi / 2),
    (5, 4, np.pi / 2),
    (5, 6, np.pi / 2),
    (3, 2, np.pi / 4),   
    (3, 2, 0),           
]

fig, axes = plt.subplots(2, 4, figsize=(12, 6.5))

for ax, (a, b, delta) in zip(axes.ravel(), cases):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    ax.plot(x, y, lw=1)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(fr"$a:b$ = {a}:{b},  $\delta$ = {delta/np.pi:.2f}$\pi$", fontsize=10)

fig.suptitle("Lissajous curves", fontsize=14)

plt.savefig("/home/badhon/python/lissajous.jpg", dpi=600)
plt.show()
