# incomplete........................................................

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

v_in = np.arange(0, 20+.5, 1)

v1_o = np.array([0.00, 0.41, 1.54, 2.57, 3.66, 4.78, 5.86, 6.96, 7.66, 7.77, 7.83, 7.87, 7.91, 7.94, 7.98, 8.01, 8.04, 8.07, 8.10, 8.13, 8.16])

v2_o = np.array([0.00, 0.57, 1.63, 2.72, 3.67, 4.86, 5.87, 6.96, 7.93, 8.69, 8.78, 8.85, 8.90, 8.95, 8.99, 9.02, 9.06, 9.10, 9.13, 9.16, 9.19])

v3_o = np.array([0.00, 0.60, 1.63, 2.72, 3.67, 4.86, 5.95, 6.92, 7.96, 9.06, 9.69, 9.79, 9.85, 9.91, 9.96, 10.00, 10.04, 10.08, 10.12, 10.16, 10.19])

v4_o = np.array([0.00, 0.53, 1.63, 2.57, 3.64, 4.76, 5.80, 6.90, 7.86, 9.09, 10.12, 11.05, 11.78, 11.88, 11.95, 12.01, 12.07, 12.12, 12.17, 12.22, 12.26])

# def func(x, a, b, c, d):
#     return a*x**(1./5)+b*x**2-c*x+d

fig, ax = plt.subplots()

ax.set_title('Graph of Different Regulated Voltages', fontsize=15)
ax.set_xlabel(r'$V_{out}$ (Volt)', fontsize=12)
ax.set_ylabel(r'$V_{in}$ (Volt)', fontsize=12)

ax.plot(v_in, v1_o, '.', label=r'$V_{reg} = $8V')
ax.plot(v_in, v2_o, '.', label=r'$V_{reg} = $9V')
ax.plot(v_in, v3_o, '.', label=r'$V_{reg} = $10V')
ax.plot(v_in, v4_o, '.', label=r'$V_{reg} = $12V')

# popt0, pcov0 = curve_fit(func, v_in, v1_o, maxfev=10000)
# xfit = np.linspace(0, max(v_in), 1000)
# ax.plot(xfit, func(xfit, popt0[0], popt0[1], popt0[2], popt0[3]))

# popt1, pcov1 = curve_fit(func, v_in, v2_o, maxfev=10000)
# ax.plot(xfit, func(xfit, popt1[0], popt1[1], popt1[2], popt1[3]))

# popt2, pcov2 = curve_fit(func, v_in, v3_o, maxfev=10000)
# ax.plot(xfit, func(xfit, popt2[0], popt2[1], popt2[2], popt2[3]))

# popt3, pcov3 = curve_fit(func, v_in, v4_o, maxfev=10000)
# ax.plot(xfit, func(xfit, popt3[0], popt3[1], popt3[2], popt3[3]))

ax.grid(which='Major')
ax.grid(which='Minor', linestyle='dotted')
ax.minorticks_on()
ax.legend(loc='upper left', fontsize=12)
plt.savefig('/home/badhon/python/4th_year/voltage_regulation.png', dpi=2000)
plt.show()
