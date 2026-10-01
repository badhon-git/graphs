import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit 

T1_c = np.arange(100, 40-1, -4)
V1 = np.array([33.5, 39.4, 44.7, 49.6, 56.6, 62.0, 68.3, 73.8, 80.3, 86.5, 92.8, 100.7, 107.5, 114.7, 121.6, 128.4])

T2_c = np.arange(128, 40-1, -4)
V2 = np.array([165.9, 178.9, 187.4, 197.5, 207.5, 217.2, 227.0, 236.8, 249.2, 257.3, 265.8, 274.4, 284.7, 294.4, 305.4, 311.5, 321.4, 330.1, 339.3, 347.6, 355.5, 364.7, 373.2])

T1_k = T1_c + 273.15
print('T_G(K) = ', T1_k)
T2_k = T2_c + 273.15
print('T_S(K)', T2_k)

def func(x, m, c):
    return m*x+c
popt, pcov = curve_fit(func, T1_k, V1)
xfit = np.linspace(0, max(T1_k)+100, 1000)

def func1(x, m, c):
    return m*x+c
popt1, pcov1 = curve_fit(func1, T2_k, V2)
xfit1 = np.linspace(0, max(T2_k)+100, 1000)

fig, ax = plt.subplots()

ax.plot(xfit, func(xfit, *popt), '-', label='Germanium')
ax.plot(xfit1, func1(xfit1, *popt1), '-', label='Silicon')

ax.plot(T1_k, V1, '.', color='r')
ax.plot(T2_k, V2, '.', color='g')

ax.set_xlim(0, 500)
ax.set_ylim(0, 1200)

Eg_G = popt[1]*1e-3
Eg_S = popt1[1]*1e-3
print('Energy band gap of Germanium = ', Eg_G, 'eV')
print('Energy band gap of Silicon = ', Eg_S, 'eV')

ax.set_title('Energy Band Gap', fontsize=15)
ax.set_xlabel('T (K)', fontsize=12)
ax.set_ylabel('V (mV)', fontsize=12)

ax.grid(which='Major', color='gray')
ax.grid(which='Minor', linestyle='dotted')
ax.minorticks_on()

ax.legend()
fig.savefig('/home/badhon/python/4th_year/band_gap.jpg', dpi=2000)
plt.show()
