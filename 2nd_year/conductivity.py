# incomplete.....

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.5, 22.5+0.1, 0.5)
theta = np.array([67.5, 67, 66, 65.5, 65, 64.5, 64, 63.5, 63, 62.5, 62, 61.5, 61, 60.5, 60, 59.5, 59, 58, 57.5, 57, 56.5, 56, 56, 55.5, 55, 54.5, 54, 54, 53.5, 53, 53, 52.5, 52, 52, 51, 51, 50.5, 50, 50, 49.5, 49, 49, 49, 48.5, 48])

plt.title('Thermal Conductivity')
plt.ylabel('Temperature (C)')
plt.xlabel('Time (min)')

plt.plot(t, theta,'.')
plt.show()
