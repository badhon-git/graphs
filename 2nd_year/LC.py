import matplotlib.pyplot as plt
import numpy as np

f = np.arange(100, 1000+10, 100)
L = np.array([44.12, 102.94, 161.76, 223.88, 272.73, 333.33, 384.62, 453.13, 507.94, 555.56])
C = np.array([1392.16, 682.54, 454.55, 358.36, 268.66, 223.88, 179.10, 164.18, 134.33, 119.40])

plt.title('Variation of resistance with frequency')
plt.xlabel('Frequency in HZ')
plt.ylabel('Frequency in ohm')

plt.plot(f, L, '.-', label='Due to L')
plt.plot(f, C, '.-', label='Due to C')
plt.savefig('LC.jpg')
plt.legend()
plt.show()
