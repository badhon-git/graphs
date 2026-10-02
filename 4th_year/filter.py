# incomplete... need a function for bandpass  

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Low pass filter..............................................................

f1 = np.arange(50, 1000+1, 50)
f2 = np.arange(1500, 5000+1, 500)

f_l = np.hstack((f1, f2, [6000]))
# print(f_l)

A_l = np. array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.99, 0.98, 0.95, 0.93, 0.89, 0.86, 0.82, 0.78, 0.72, 0.69, 0.64, 0.61, 0.58, 0.54, 0.29, 0.17, 0.11, 0.08, 0.06, 0.05, 0.04, 0.03, 0.03])

fig, ax = plt.subplots()

ax.set_xscale('log')

ax.plot(f_l, A_l, '.')
ax.plot(f_l, A_l, '-')

# ax.set_xlim(1e1, 1e4)
ax.set_ylim(0, 1.4)

ax.set_title('Low pass filter', fontsize=15)
ax.set_xlabel(r'Frequency, $f$ (HZ)', fontsize=12)
ax.set_ylabel(r'Relative voltage gain, $A_N$ (dB)', fontsize=12)

ax.grid(which='major', color='gray')
ax.grid(which='minor', linestyle='dotted')
ax.minorticks_on()

fig.savefig('/home/badhon/python/4th_year/lowpass.png', dpi=2000)

# High pass filter..............................................................

f3 = f1[1:]
# print[f3]

f_h = np.hstack((f3, f2, [5500, 6000]))
A_h = np.array([0.04, 0.04, 0.06, 0.09, 0.14, 0.19, 0.23, 0.27, 0.33, 0.38, 0.42, 0.48, 0.52, 0.58, 0.60, 0.65, 0.68, 0.72, 0.75, 0.92, 0.97, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])

fig1, ax = plt.subplots()

ax.set_xscale('log')

ax.plot(f_h, A_h, '.')
ax.plot(f_h, A_h, '-')

ax.set_ylim(0, 1.4)

ax.set_title('High pass filter', fontsize=15)
ax.set_xlabel(r'Frequency, $f$ (HZ)', fontsize=12)
ax.set_ylabel(r'Relative voltage gain, $A_N$ (dB)', fontsize=12)

ax.grid(which='major', color='gray')
ax.grid(which='minor', linestyle='dotted')
ax.minorticks_on()

fig1.savefig('/home/badhon/python/4th_year/highpass.png', dpi=2000)

# Band pass filter.....................................................................

f4 = f1[3:]
# print(f4)
f5 = f2[:-2]
# print(f5)

f_b = np.hstack((f4, f5, [5000, 6000]))
A_b = np.array([0.1, 0.1, 0.12, 0.12, 0.18, 0.21, 0.24, 0.33, 0.37, 0.48, 0.61, 0.77, 0.9, 1.0, 0.98, 0.74, 0.66, 0.22, 0.15, 0.12, 0.1, 0.08, 0.07, 0.06, 0.05])

# def g(x, a, b, sigma):
#    return a*np.exp(-(x-b)**2/(2*sigma**2)) 

# popt, pcov = curve_fit(g, f_b, A_b)
# xfit = np.linspace(min(f_b), max(f_b), 1000)

fig2, ax = plt.subplots()

ax.set_xscale('log')

ax.plot(f_b, A_b, '.')
ax.plot(f_b, A_b, '-')
# ax.plot(xfit, g(xfit, popt[0], popt[1], popt[2]))

ax.set_ylim(0, 1.4)

# ughhhhhh........................................
# sokale ct ;( pore korbo!

ax.set_title('Band pass filter', fontsize=15)
ax.set_xlabel(r'Frequency, $f$ (HZ)', fontsize=12)
ax.set_ylabel(r'Relative voltage gain, $A_N$ (dB)', fontsize=12)

ax.grid(which='major', color='gray')
ax.grid(which='minor', linestyle='dotted')
ax.minorticks_on()

fig2.savefig('/home/badhon/python/4th_year/bandpass.png', dpi=2000)

plt.show()
