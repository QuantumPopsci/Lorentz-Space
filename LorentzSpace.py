import numpy as np
from matplotlib import pyplot as plt


sigma = 10
rho = 28
beta = 8/3

x0 = 30
y0 = 30
z0 = 30


variation = 0.2


t = np.linspace(0, 20, 10000)


def solve_lorenz(initial_x, initial_y, initial_z):
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    z = np.zeros_like(t)
    x[0] = initial_x
    y[0] = initial_y
    z[0] = initial_z

    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        x[i] = x[i-1] + sigma * (y[i-1] - x[i-1]) * dt
        y[i] = y[i-1] + (rho * x[i-1] - y[i-1] - x[i-1] * z[i-1]) * dt
        z[i] = z[i-1] + (x[i-1] * y[i-1] - beta * z[i-1]) * dt
    return x, y, z


x1, y1, z1 = solve_lorenz(x0, y0, z0)
x2, y2, z2 = solve_lorenz(x0 + variation, y0, z0)
x3, y3, z3 = solve_lorenz(x0, y0, z0 - variation)


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')


ax.plot(x1, y1, z1, label='Original', color='b', linewidth=0.5)
#ax.plot(x2, y2, z2, label='x+'+str(variation), color='g', linewidth=0.5)
ax.plot(x3, y3, z3, label='z-'+str(variation), color='r', linewidth=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz System - Initial Condition Variations')
ax.legend()

plt.tight_layout()
plt.show()
