import matplotlib.pyplot as plt
import numpy as np

concentration = np.arange(5, 30+1, 5)
theta = np.array([3.8, 7.9, 12.0, 14.9, 19.6, 21.8])

poly = np.polyfit(concentration, theta, deg=1)
f = np.poly1d(poly)
x = np.linspace(0, max(concentration), 1000)
y = f(x)

plt.title('Suger Solution')
plt.ylabel('Rotation in deg')
plt.xlabel('concentration in %')

plt.plot(x, y)
plt.plot(concentration, theta, '.')
plt.savefig('suger.jpg')
plt.show()
