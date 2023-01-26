"""Projected Gradient Descent - Example 1

created by Zekai Liang
July 28, 2022

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,100)
y = np.linspace(-2,2,100)

X, Y = np.meshgrid(x,y)

Z = X + np.multiply(X,Y) + (1+Y)**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X,Y,Z, cmap="plasma")
plt.show()