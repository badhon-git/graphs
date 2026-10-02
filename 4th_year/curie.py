# incomplete.......................................

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks

t = np.arange(400, 55-1, -5)
v = np.array([3.63, 3.62, 3.61, 3.59, 3.58, 3.56, 3.55, 3.54, 3.53, 3.52, 3.51, 3.51, 3.50, 3.50, 3.49, 3.48, 3.48, 3.48, 3.48, 3.48, 3.48, 3.46, 3.47, 3.48, 3.49, 3.50, 3.52, 3.54, 3.56, 3.62, 3.64, 3.67, 3.72, 3.78, 3.84, 3.92, 4.02, 4.16, 4.29, 4.47, 4.70, 4.99, 5.44, 6.00, 6.62, 7.14, 7.54, 7.87, 8.19, 8.44, 8.72, 8.98, 9.25, 9.49, 9.72, 9.93, 10.16, 10.42, 10.63, 10.82, 10.95, 11.13, 11.31, 11.49, 11.65, 11.81, 11.94, 12.04, 11.23, 12.37])

t2 = np.arange(400, 60-1, -5)
dt = 5
dv1 = []
for i in range(1, len(v)):
    x = v[i] - v[i-1]
    dv1.append(x)
# print('dv = ', dv1)
print('dv = ', abs(np.around(dv1, 5)))


dvdt = []
for x in dv1:
    dvdt.append(x/dt)
print('dv/dt = ', abs(np.around(dvdt, 5)))

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()


# ..................................................
# def func(x, a, b):
#   return a*np.exp(-b*x)

# popt, pcov = curve_fit(func, t, v, maxfev=10000)
# xfit = np.linspace(max(t), min(t), 1000)
# ..................................................


poly1 = np.polyfit(t, v, deg=13)
f = np.poly1d(poly1)
x1 = np.linspace(400, 70, 10000)
y1 = f(x1)
ax1.plot(x1, y1)


# .......................................................
# def func1(x, a, b):
#   return b**2+a*np.exp(-1.0*(x - 185)**2)

# popt, pcov = curve_fit(func1, t2, dvdt, maxfev=100000)
# xfit = np.linspace(max(t2), min(t2), 1000)


# peaks, info = find_peaks(dvdt)
# T_c = info['left_ips']
# np.trapz(dvdt[T_c])
# print(peaks)

# Gaussian function
# def gaussian(x, a, b, sigma, c):
#     return c+a*np.exp(-np.power(x-b, 2.)/(2*np.power(sigma, 2.)))
# popt, pcov = curve_fit(gaussian, t2, dvdt, maxfev=10000)
# xfit = np.linspace(max(t2), min(t2), 1000)
# ax2.plot(xfit, gaussian(xfit, *popt), '-')

# def g(x, a, b, sigma):
#     return a*np.exp(-(x-b)**2/sigma**2)

# dhurrrrrr..................................................... 

ax2.set_ylim(-0.02, 0.14)

ax1.grid(which='major', color='gray')
ax1.grid(which='minor', linestyle='dotted')
# ax2.grid(which='major', color='gray')
# ax2.grid(which='minor', linestyle='dotted')
ax1.minorticks_on()
ax2.minorticks_on()

ax1.set_xlabel(r'$T(\degree$C)', fontsize=12)
ax1.set_ylabel(r'$V_s$(V)', fontsize=12)
ax2.set_ylabel(r'$dv/dt$ (V/$\degree$C)', fontsize=12)

# ax2.plot(xfit, func1(xfit, *popt), '-')
ax1.plot(t, v, '.b', label=r'$V_s$ ~ $T$')
ax1.legend(loc='center right')
ax2.plot(t2, dvdt, '.r', label=r'$dv/dt$ ~ $T$')
ax2.legend(loc='best')
ax1.grid(which='Major', color='black')

plt.title('Curie Temperature', fontsize=15)

plt.savefig('/home/badhon/python/4th_year/curie.png', dpi=2000, bbox_inches='tight')
plt.show()
