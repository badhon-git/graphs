import matplotlib.pyplot as plt
import numpy as np

vi = np.array([0.5, 1, 2, 3, 4, 6, 8, 11, 13, 15, 18])
vo = np.array([0.5, 1, 2, 3, 3.5, 4.1, 4.3, 4.5, 4.7, 4.8, 5])

poly = np.polyfit(vi, vo, deg=4)
f = np.poly1d(poly)
x = np.linspace(0, 18.5, 1000)
y = f(x)

plt.plot(x, y)
plt.plot(vi, vo, '.')

plt.show()
