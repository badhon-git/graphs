import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
from scipy.optimize import curve_fit

# calculations...........................................

b = np.array([13, 14, 18, 15, 11])
bg = mean(b)
print('background', bg)

r = np.arange(6, 22+1, 2)
r2 = np.array(r**2)
r22 = np.array(1/r2)
print('r^2 = ', r2)
print('1/r^2 = ', r22)

# Data for known source..........

print('For known source:')

R1 = np.array([[200, 193, 209], [125, 122, 119], [87, 88, 92], [69, 67, 62], [56, 61, 59], [46, 46, 39], [37, 34, 38], [32, 34, 33], [26, 26, 34]])

R1_avg = np.array([mean(R1[i]) for i in range(0, len(R1))])
print('Average activity ', R1_avg)
R1_corr = np.array(R1_avg - bg)
print('Corrected activity ', R1_corr)

# Data for unknown source........

print('For unknown source:')

R2 = np.array([[133, 132, 139], [87, 100, 91], [72, 63, 65], [51, 58, 49], [42, 43, 43], [35, 37, 35], [34, 36, 26], [32, 27, 33], [22, 30, 26]])

R2_avg = np.array([mean(R2[i]) for i in range(0, len(R2))])
print('Average activity ', R2_avg)

R2_corr = np.array(R2_avg - bg)
print('Corrected activity ', R2_corr)

# graphs................................................

# linear graph..........

def func(x, m, c):
    return m*x+c

fig, ax = plt.subplots()

popt1, pcov1 = curve_fit(func, r22, R1_corr)
popt2, pcov2 = curve_fit(func, r22, R2_corr)

xfit1 = np.linspace(min(r22), max(r22), 1000)
xfit2 = np.linspace(min(r22), max(r22), 1000)

ax.set_xlim(0, 0.03)
ax.set_ylim(0, 200)

ax.plot(r22, R1_corr, '.', label='Known source')
ax.plot(r22, R2_corr, '.', label='Unknown source')

ax.plot(xfit1, func(xfit1, popt1[0], popt1[1]), label='For known source')
ax.plot(xfit2, func(xfit2, popt2[0], popt2[1]), label='For unknown source')

ax.set_title(r'R ~ 1/r$^2$ graph', fontsize=15)
ax.set_xlabel(r'1/r$^2$(cm$^{-2}$)', fontsize=12)
ax.set_ylabel('R(cpm)', fontsize=12)

ax.grid(which='major', color='gray')
ax.grid(which='minor', linestyle='dotted')
ax.minorticks_on()
ax.legend()
fig.savefig('/home/badhon/python/4th_year/inverse_linear.png', dpi=2000)

#log-log graph..........

def func2(x, a, b):
    return a / x**b

fig1, ax = plt.subplots()

popt, pcov = curve_fit(func2, r, R1_corr, maxfev=100000)
xfit2 = np.linspace(min(r), max(r), 1000)

ax.plot(xfit2, func2(xfit2, *popt))

ax.set_xscale('log')
ax.set_yscale('log')

ax.plot(r, R1_corr, '.')

ax.set_title('R ~ r graph', fontsize=15)
ax.set_xlabel('r (cm)', fontsize=12)
ax.set_ylabel('R (cpm)', fontsize=12)

ax.grid(which='major', color='gray')
ax.grid(which='minor', linestyle='dotted')
ax.minorticks_on()
fig1.savefig('/home/badhon/python/4th_year/inverse_log.png', dpi=2000)

# result....................................................

print('slope of the line = ', -popt[1])
print('strength of unknown source = ', popt2[0]/popt1[0]*5*np.exp(-0.0229*14.30))

plt.show()
