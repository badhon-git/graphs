import numpy as np
import matplotlib.pyplot as plt

#   psi_n(x) = sqrt(2/L) * sin(n*pi*x/L)
#   E_n      = n^2 * pi^2 * hbar^2 / (2*m*L^2)

L = 1.0
x = np.linspace(0, L, 1000)
levels = [1, 2, 3, 4, 5]

def psi(n, x):
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

def energy(n):
    return n**2 * np.pi**2 / (2 * L**2)

# Wavefunctions................................................................

fig, ax = plt.subplots()

for n in levels:
    ax.plot(x, psi(n, x), label=f'n = {n}')

ax.axhline(0, color='k', lw=0.8)

ax.set_title(r'Wavefunctions $\psi_n(x)$', fontsize=15)
ax.set_xlabel(r'Position, $x/L$', fontsize=12)
ax.set_ylabel(r'$\psi_n(x)$', fontsize=12)

ax.legend()
ax.minorticks_on()

fig.savefig('/home/badhon/python/wavefunctions.jpg', dpi=600)

# Energy levels................................................................

fig1, ax = plt.subplots()

scale = 16.0   
for n in levels:
    En = energy(n)
    ax.hlines(En, 0, L, color='gray', lw=0.8)
    ax.plot(x, En + scale * psi(n, x) / np.sqrt(2 / L) * 0.5)
    lab = r'$E_1$' if n == 1 else rf'$E_{n} = {n**2}E_1$'
    ax.text(L * 1.02, En, lab, va='center', fontsize=10)

ax.set_xlim(0, 1.3)

ax.set_title(r'Energy levels ($E_n \propto n^2$)', fontsize=15)
ax.set_xlabel(r'Position, $x/L$', fontsize=12)
ax.set_ylabel(r'Energy, $E$ ($\hbar^2/mL^2$)', fontsize=12)

ax.minorticks_on()

fig1.savefig('/home/badhon/python/energy_levels.jpg', dpi=600)

plt.show()
