import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from statistics import mean

t = np.array([0.0, 1.1, 2.3, 3.4, 4.6, 6.1, 7.2, 8.5, 9.8])
R = np.array([[10361, 10565, 10557], [7197, 7295, 7187], [6279, 6264, 6258],
             [5641, 5600, 5553], [5007, 5049, 5128], [4698, 4640, 4602],
             [4212, 4243, 4331], [4084, 3948, 3903], [3682, 3652, 3674]])

R_avr = np.array([mean(R[i]) for i in range(0, len(R))])
print('Average Activity : ', R_avr)

background = np.array([200, 202, 202])
R_crt = np.array(R_avr - mean(background))
print('Corrected Activity : ', R_crt)

def func(x, a, b):
    return a*np.exp(-b*x)

def func1(x, c, d, g, h):
    return c*np.exp(-d*x)+g*np.exp(-h*x)

popt, pcov = curve_fit(func, t, R_crt, maxfev=100000)
popt1, pcov1 = curve_fit(func1, t, R_crt, maxfev=100000000)

xfit = np.linspace(max(t), min(t), 10000)

print(popt)
print(popt1)

fig, ax = plt.subplots()

ax.set_title('Absorption of Gamma rays',  fontsize=15)
ax.set_xlabel('X (mm)', fontsize=12)
ax.set_ylabel('R (cpm)', fontsize=12)
ax.grid(which='major', color='gray')
ax.grid(which='minor', linestyle='dotted')
ax.minorticks_on()

ax.plot(xfit, func(xfit, *popt), '-')
ax.plot(xfit, func1(xfit, *popt1), '-', label=r'Fit for $\gamma$ ray absorption')
ax.plot(t, R_crt, '.')
plt.legend()
plt.savefig('/home/badhon/python/3rd_year/absorption.png', dpi=1000)
plt.show()
