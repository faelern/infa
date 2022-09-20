import math
import random
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    # return 2*x+1
    return np.sin(x)


rect_width = 5
rect_height = 5
rect_area = rect_width * rect_height
hits = 0

plot_x = np.arange(-rect_width, rect_width, 0.1)

# plot_y = 2 * plot_x + 1
plot_y = np.sin(plot_x)
plt.ylim([-rect_height, rect_height])
plt.plot(plot_x, plot_y)


x = []
y = []
colors = []
# samples = int(input('Podaj liczbe prob'))
samples = 1000
for i in range(samples):
    x_test = random.uniform(-rect_width, rect_width)
    x.append(x_test)
    y_test = random.uniform(-rect_height, rect_height)
    y.append(y_test)
    if f(x_test) > y_test:
        colors.append('green')
        hits += 1
    else:
        colors.append('red')

plt.scatter(x, y, s=7, c=colors)
area = rect_area * hits / samples
print(area)
plt.show()
