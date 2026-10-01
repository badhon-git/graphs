import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

v = np.array([76, 82, 94, 104, 118, 130, 145, 169, 182, 204, 224])
r = np.arange(3.00e-2, 5.50e-2+1e-3, 0.25e-2)
r2 = np.array(r**2)
print('r^(-2) = ', r2)

N = 130
R = 0.15
i = 1.25
B = (8.99e-7*N*i)/R

B2 = B**2
em = np.array([2*v/(B2*r2)])
print('e/m = ', em)


def func(x, m, c):
    return m*x+c


popt, pcov = curve_fit(func, v, r2)
print(popt)
xfit = np.arange(min(v)-10, max(v)+10, 0.01)

em2 = 2/(B2*popt[0])
print('Value of e/m from graph : {}C/Kg'.format(em2))

fig, ax = plt.subplots()
ax.grid(which='major', linestyle='-', color='Black')
ax.grid(which='minor', linestyle='dotted')
ax.minorticks_on()

ax.plot(xfit, func(xfit, *popt), label='m = %1e, c = %1e' % tuple(popt))
ax.plot(v, r2, '.')
ax.set_title('Graph for e/m Calculation', fontsize=15)
ax.set_xlabel('V$_a$(volt)', fontsize=12)
ax.set_ylabel('r$^2$(m$^2$)', fontsize=12)
ax.legend()
plt.savefig('/home/badhon/python/3rd_year/em.png', dpi=2000, bbox_inches='tight')
plt.show()
