import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)

y = 2 * x + 1
plt.ylim([0, 10])
plt.plot(x, y)

x = [1, 2]

y = [3, 4]

plt.scatter(x, y, facecolor='red')

plt.show()