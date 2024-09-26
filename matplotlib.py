
import matplotlib.pyplot as plt #pyplot submodule
import numpy as np

xpoints = np.array([0,23,34,67,78]) 
ypoints = np.array([0,34,67,88,23])

plt.scatter(xpoints, ypoints, color='purple', marker='x')
plt.show()
