import numpy as np
import matplotlib.pyplot as plt

d = np.array([0, 1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.3, 8.3, 9.3, 10.4, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.6, 19.6, 20.7])

n = np.array([0, 10.08, 20.24, 27.26, 32.49, 36.40, 40.26, 43.19, 46.25, 48.95, 52.93, 55.90, 57.89, 58.50, 60.00, 60.33, 61.70, 65.32, 64.52, 63.68])

fig, ax = plt.subplots()


# def func(x1, x2, a, b, c):

poly = np.polyfit(d, n, deg=4)
f = np.poly1d(poly)
x1 = np.linspace(0, 22, 1000)
y1 = f(x1)
ax.plot(x1, y1)

ax.grid(which='Major', color='gray')
ax.grid(which='Minor', linestyle='dotted')
ax.minorticks_on()

ax.set_xlim(0, 25)
ax.set_ylim(0,70)

ax.set_title('Efficiency of GM tube', fontsize=15)
ax.set_xlabel('d (cm)', fontsize=12)
ax.set_ylabel(r'$\eta$(%)', fontsize=12)
ax.legend()

ax.plot(d, n, '.')
plt.savefig('/home/badhon/python/4th_year/efficiency.jpg', dpi=1000)
plt.show()
