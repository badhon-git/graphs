import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.axvline(x = 0.58, color = 'r', linestyle = '-', label=r'$Q1=Q2=Q3=c$')
plt.axvline(x = 0.63, color = 'g', label=r'$Q1=Q2=c,Q3=b$')
plt.axvline(x = 0.68, color = 'b', label=r'$Q1=c,Q2=Q3=b$')
plt.axvline(x = 0.73, color = 'orange', label=r'$Q1=Q2=Q3=b$')

s = np.linspace(0.1, 0.9, 1000)
t = np.linspace(0.2, 0.8, 1000)

plt.plot(s, t, '-', color = 'black', label=r'$m(qqQ)+m(Q\bar Q)$')

#plt.plot(s, t, '-', color = 'black')

s2 = np.linspace(0.1, 0.9, 1000)
t2 = np.linspace(0.3, 0.7, 1000)
plt.plot(s2, t2, '--', color = 'gray', label=r'$m(qqQQ\bar Q)$')

#plt.plot(s2, t2, '--', color = 'gray')

ax = plt.gca()

ax.xaxis.set_tick_params(labelbottom = False)
ax.yaxis.set_tick_params(labelleft = False)
ax.set_xticks([])
ax.set_yticks([])

plt.xlabel('m (Q)')
plt.ylabel('m (hadron)')
plt.legend(loc = 'lower right')

plt.xlim(0, 1.2)
plt.ylim(0, 1.2)

plt.savefig('/home/badhon/python/bps/bps3.png', dpi = 600)

plt.show()

