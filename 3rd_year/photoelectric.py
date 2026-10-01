import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

v = np.array([0.61, 0.68, 0.80, 0.98, 1.13])
nu = np.array([5.22, 5.50, 5.94, 6.67, 7.32])

fig, ax = plt.subplots()


def func(x, m, c):
    return m*x+c


popt, pcov = curve_fit(func, nu, v)
print(popt)
xfit = np.arange(0, max(nu)+0.3, 0.1)

e = 1.60217663e-19
h = popt[0]*1e-14*e
phi = -popt[1]
print('h = ', h, 'Js')
print('phi = ', phi, 'eV')

ax.grid(which='Major', color='Black')
ax.grid(which='minor', linestyle='dotted')
ax.minorticks_on()

ax.set_xlim(0, 8)
ax.set_ylim(-0.75, 1.25)

ax.set_title('Stopping Potential', fontsize=15)
ax.set_xlabel(r'$\nu$ (10$^{14}$ Hz)', fontsize=12)
ax.set_ylabel('V (volt)', fontsize=12)
ax.plot(xfit, func(xfit, *popt), color='g', label='m=%4.3fe-14, c=%4.3f' % tuple(popt))
ax.plot(nu, v, '.', color='r')
ax.legend()
plt.savefig('/home/badhon/python/3rd_year/photoelectric.png', dpi=1000)
plt.show()
