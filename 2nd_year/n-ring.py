import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 10+0.5, 1)

yd = np.array([9.8, 12.0, 13.7, 14.7, 16.2, 17.1, 18.2, 19.7, 20.2, 20.8])
yr = np.array(yd/2)
yr2 = np.array(yr**2)
print('gr ', yr, 'yr^2', yr2)

gd = np.array([9.4, 11.3, 13.0, 14.5, 15.8, 16.8, 17.9, 18.7, 19.6, 20.2])
gr = np.array(gd/2)
gr2 = np.array(gr**2)
print('gr ', gr, 'gr^2 ', gr2)

bd = np.array([8.6, 10.8, 12.6, 13.6, 15.0, 16.0, 17.2, 18.1, 18.5, 19.2])
br = np.array(bd/2)
br2 = np.array(br**2)
print('br ', br, 'br^2 ', br2)

poly1 = np.polyfit(n, yr2, deg=1)
poly2 = np.polyfit(n, gr2, deg=1)
poly3 = np.polyfit(n, br2, deg=1)

f1 = np.poly1d(poly1)
f2 = np.poly1d(poly2)
f3 = np.poly1d(poly3)

x = np.linspace(min(n), max(n), 1000)

y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

plt.xlabel('n')
plt.ylabel('r^2 (mm)')

plt.plot(x, y1, color='y')
plt.plot(x, y2, color='g')
plt.plot(x, y3, color='b')

plt.plot(n, yr2, '.', label='yellow', color='orange')
plt.plot(n, gr2, '.', label='green', color='olive')
plt.plot(n, br2, '.', label='blue', color='navy')

plt.savefig('n-ring.jpg')
plt.legend()
plt.show()
