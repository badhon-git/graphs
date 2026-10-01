import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#plt.axvline(x = 0.43, color = 'r', linestyle = '-', label=r'$Q1=Q2=Q3=c$', linewidth=0.75)
#plt.axvline(x = 0.48, color = 'g', label=r'$Q1=Q2=c,Q3=b$', linewidth=0.75)
#plt.axvline(x = 0.53, color = 'b', label=r'$Q1=c,Q2=Q3=b$', linewidth=0.75)
#plt.axvline(x = 0.58, color = 'orange', label=r'$Q1=Q2=Q3=b$', linewidth=0.75)

s = np.linspace(0.1, 0.9, 1000)
t = np.linspace(0.15, 0.78, 1000)

plt.plot(s, t, '-', color = 'black', label=r'$m(qqQ)+m(Q\overline{Q})$')

#plt.plot(s, t, '-', color = 'black', linewidth=0.75)

s2 = np.linspace(0.1, 0.9, 1000)
t2 = np.linspace(0.3, 0.8, 1000)
plt.plot(s2, t2, '--', color = 'gray', label=r'$m(qqQQ\overline{Q})$')

#plt.plot(s2, t2, '--', color = 'gray', linewidth=0.75)

ax = plt.gca()

ax.xaxis.set_tick_params(labelbottom = False)
ax.yaxis.set_tick_params(labelleft = False)
ax.set_xticks([])
ax.set_yticks([])

plt.xlabel('m (Q)')
plt.ylabel('m (hadron)')
plt.legend(loc = 'upper right')

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.savefig('/home/badhon/python/bps/bps0.png', dpi=600)

plt.show()

