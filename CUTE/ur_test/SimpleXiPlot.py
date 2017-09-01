import numpy as np
import matplotlib.pyplot as plt



raw_data = "./results/2pcf_results.dat"

s, xi = np.loadtxt(raw_data, delimiter=' ', usecols=(0, 1), unpack=True)

xi = xi * s * s

plt.scatter(s, xi)
plt.show()