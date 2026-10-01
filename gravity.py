import numpy as np
import matplotlib.pyplot as plt

# g(r) = G * M(r) / r^2
# M(r) = \int 4*\pi*r'^2 * \rho(r') dr'.

G = 6.674e-11
R = 6.371e6                             

r = np.linspace(1, R, 20000) 
x = r / R

km = r / 1e3
conds = [km < 1221.5,
         (km >= 1221.5) & (km < 3480.0),
         (km >= 3480.0) & (km < 5701.0),
         (km >= 5701.0) & (km < 5771.0),
         (km >= 5771.0) & (km < 5971.0),
         (km >= 5971.0) & (km < 6151.0),
         (km >= 6151.0) & (km < 6346.6),
         (km >= 6346.6) & (km < 6356.0),
         (km >= 6356.0) & (km < 6368.0),
         km >= 6368.0]
funcs = [lambda x: 13.0885 - 8.8381 * x**2,
         lambda x: 12.5815 - 1.2638 * x - 3.6426 * x**2 - 5.5281 * x**3,
         lambda x: 7.9565 - 6.4761 * x + 5.5283 * x**2 - 3.0807 * x**3,
         lambda x: 5.3197 - 1.4836 * x,
         lambda x: 11.2494 - 8.0298 * x,
         lambda x: 7.1089 - 3.8045 * x,
         lambda x: 2.6910 + 0.6924 * x,
         lambda x: 2.900 + 0 * x,
         lambda x: 2.600 + 0 * x,
         lambda x: 1.020 + 0 * x]

rho = np.piecewise(x, conds, funcs) * 1e3   

dm = 4 * np.pi * r**2 * rho
M = np.concatenate(([0], np.cumsum(0.5 * (dm[1:] + dm[:-1]) * np.diff(r))))

g_real = G * M / r**2
g_uniform = G * M[-1] / R**3 * r

print(f"Earth mass: {M[-1]:.3e} kg   (real: 5.972e24 kg)")
print(f"g at surface: {g_real[-1]:.2f} m/s^2")
print(f"max g: {g_real.max():.2f} m/s^2 at depth {(R - r[g_real.argmax()])/1e3:.0f} km")

depth = (R - r) / 1e3

fig, ax = plt.subplots()
ax.plot(depth, g_real, label = 'Real Earth')
ax.plot(depth, g_uniform, '--', label = 'Uniform density')

ax.set_xlim(0, 6371)
ax.set_ylim(0, 11)
ax.set_title('Gravity inside the Earth', fontsize=15)
ax.set_xlabel(r'Depth below surface (km)', fontsize=12)
ax.set_ylabel(r'$g$ (m/s$^2$)', fontsize=12)
ax.minorticks_on()
ax.legend()

fig.savefig('/home/badhon/python/gravity_vs_depth.jpg', dpi=600)
plt.show()
