import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.linspace(-5, 2, 500)
x2 = np.linspace(0.15, 3.8, 500)

x0, y0 = 0, 10
x1, y1 = 3, 1

y = 0.2 + np.exp(x)
y2 = 0.2 + y0 * np.exp(-2 * x2)
#y = -0.8 + 2**(x)**2  
#k = -np.log(y1 / y0) / (x1 - x0)
#y2 = -0.2 + y0 * np.exp(-k * x2)
#y2 = 0.2 + y0 * np.exp(-2 * x2)
#y2 = 0.2 + y0 * np.exp(-3 * x2)


ax = plt.gca()
fig, ax = plt.subplots(figsize=(8, 4))
ax.xaxis.set_tick_params(labelbottom = False)
ax.yaxis.set_tick_params(labelleft = False)
ax.set_xticks([])
ax.set_yticks([])

plt.text(1.8, 0.8, 'Asymptotic freedom', fontsize=10, color='black', ha='left', va='bottom')
plt.text(0.25, 7, 'Confinement', fontsize=10, color='black', ha='left', va='bottom')

plt.plot(x, y,'--', color='chocolate', label=r'$\alpha_{QED}(q^2)$')
plt.plot(x2,y2, color='green', label=r'$\alpha_{QCD}(q^2)$')
plt.xlim(-5,4)
plt.ylim(0,8)
plt.xlabel(r'$q^2$')
plt.ylabel(r'$\alpha_{\text{eff}}(q^2)$')

plt.legend(loc='upper right')
plt.savefig('/home/badhon/python/bps/asymptotic.png', dpi=600)
plt.show()

