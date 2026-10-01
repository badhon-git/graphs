import matplotlib.pyplot as plt
import numpy as np

v = np.arange(840, 1100+1, 20)
r = np.array([[0, 0, 0], [2323, 2732, 3138], [6132, 6153, 6188], 
              [6557, 6553, 6545], [6953, 7045, 6856], [7114, 7256, 7115], 
              [7504, 7439, 7577], [7546, 7596, 7561], [7721, 7691, 7725], 
              [7698, 7752, 7750], [7880, 7955, 7944], [7988, 7893, 8091],
              [8181, 8313, 8146], [8127, 8215, 8213]])
r = np.array([np.average(r[i]) for i in range(0, len(r))])

fig, ax = plt.subplots()
poly = np.polyfit(v, r, deg=5)
f = np.poly1d(poly)
x1 = np.linspace(840, 1100, 10000)
y1 = f(x1)

ax.grid(which='Major', linestyle='-', color='Black')
ax.grid(which='Minor')
ax.set_title('Operating Voltage', fontsize=15)
ax.plot(v, r, '.')
ax.plot(x1, y1)
ax.set_xlabel('Applied Voltage (volt)', fontsize=12)
ax.set_ylabel('Count Rate (cpm)', fontsize=12)
ax.minorticks_on()
plt.savefig('/home/badhon/python/3rd_year/plateau.png', dpi=1000)
plt.show()
