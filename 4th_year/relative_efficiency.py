import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

t = np.array([0, 4.5, 6.5, 14.1, 28.1, 59.1, 102, 129, 161, 206, 258, 328, 419, 516, 590, 645])
R = np.array([6512, 5756, 5393, 4567, 3668, 1664, 1239, 815, 587, 382, 361, 341, 324, 335, 311, 339])

fig, ax = plt.subplots()

def func(x, a, b):
    return a*np.exp(-b*x)

popt, pcov = curve_fit(func, t, R)
xfit = np.linspace(min(t), max(t), 1000)
ax.plot(xfit, func(xfit, *popt), label=r'only $\beta$')

#def func1(x, a, b, c):
#    return a*np.exp(-b*x)+c

#popt1, pcov1 = curve_fit(func1, t, R)
#xfit1 = np.linspace(min(t), max(t), 1000)
#ax.plot(xfit1, func1(xfit1, popt1[0], popt1[1], popt1[2]))

def func2(x, a, b, c, d):
    return a*np.exp(-b*x)+c*np.exp(-d*x)
popt2, pcov2 = curve_fit(func2, t, R)
xfit2 = np.linspace(0, max(t), 1000)
ax.plot(xfit2, func2(xfit2, popt2[0], popt2[1], popt2[2], popt2[3]), label=r'$\beta + \gamma$')

xfit3 = np.linspace(0, max(t), 1000)
yfit3 = np.linspace(341, 339, 1000)
ax.plot(xfit3, yfit3, label=r'only $\gamma$')

ax.set_yscale('log')
ax.set_xlim(0, 700)
ax.set_ylim(1e2, 1e4)

ax.grid(which='major', color='gray')
ax.grid(which='minor', linestyle='dotted')
ax.minorticks_on()

ax.set_title('Relative efficiency', fontsize=15)
ax.set_xlabel(r'X (mg/cm$^2$)', fontsize=12)
ax.set_ylabel('R (cpm)', fontsize=12)

ax.plot(t, R, '.')
ax.legend()
fig.savefig('/home/badhon/python/4th_year/relative_efficiency.png', dpi=2000)
plt.show()
