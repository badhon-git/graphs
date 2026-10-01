import numpy as np
import matplotlib.pyplot as plt

wavelength = 500e-9  # green light
a = 10e-6                  
d = 50e-6            

theta = np.linspace(-0.06, 0.06, 4000)  # in radian
s = np.sin(theta)

interference = np.cos(np.pi * d * s / wavelength) ** 2
envelope = np.sinc(a * s / wavelength) ** 2
I = interference * envelope

fig, ax = plt.subplots()

ax.plot(theta, I, lw = 1.2, label = "double slit")
ax.plot(theta, envelope, "--", lw = 1, label = "single-slit")
ax.set_ylabel("relative intensity")
ax.set_title(fr"Double slit: $\lambda$ = {wavelength*1e9:.0f} nm, a = {a*1e6:.0f} $\mu m$, d = {d*1e6:.0f} $\mu m$")
ax.legend()

plt.tight_layout()
plt.savefig("/home/badhon/python/double_slit.png", dpi=600)
plt.show()
