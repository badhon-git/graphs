import numpy as np
import matplotlib.pyplot as plt

# GM = 1, r = 1.
# 0 < speed < 1 = ellipse (apoapsis)
# speed 1 = circular orbit
# 1 < speed < \sqrt{2} = ellipse (periapsis)
# speed \sqrt{2} = parabola (escape velocity)
# speed > \sqrt{2} = hyperbola

def acc(r):
    return -r / np.linalg.norm(r) ** 3

def rk4(r, v, dt):
    k1r, k1v = v, acc(r)
    k2r, k2v = v + 0.5*dt*k1v, acc(r + 0.5*dt*k1r)
    k3r, k3v = v + 0.5*dt*k2v, acc(r + 0.5*dt*k2r)
    k4r, k4v = v + dt*k3v, acc(r + dt*k3r)
    return (r + dt/6*(k1r + 2*k2r + 2*k3r + k4r),
            v + dt/6*(k1v + 2*k2v + 2*k3v + k4v))

dt, nsteps = 0.01, 20000

# ........................................................
# dt, nsteps = 0.01, 80000
# ........................................................

v0 = float(input("initial speed (<= 1.0): "))

r, v = np.array([1.0, 0.0]), np.array([0.0, v0])
xs = []
for _ in range(nsteps):
    r, v = rk4(r, v, dt)
    xs.append(r.copy())
xs = np.array(xs)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(xs[:, 0], xs[:, 1], lw=0.6)
ax.plot(0, 0, "ko", label="Sun")

ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.0, 1.0)

# for speed > 1.0.................................................
# ax.set_xlim(-60, 10)
# ax.set_ylim(-10, 10)
# ................................................................

ax.set_aspect("equal")
ax.set_title("Orbit")
ax.legend()

plt.tight_layout()
# plt.savefig("/home/badhon/python/1.4speed_kepler.png", dpi = 600)
plt.savefig("/home/badhon/python/kepler.png", dpi = 600)
plt.show()
