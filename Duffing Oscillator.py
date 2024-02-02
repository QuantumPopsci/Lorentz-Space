

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


alpha = 5 # Nonlinearity coefficient
beta = 0  # Damping coefficient
gamma = 0.3  # Driving force amplitude
omega = 1.2  # Driving force frequency


def duffing(x, t, alpha, beta, gamma, omega):
    return [x[1], -alpha * x[0]**3 - beta * x[1] + gamma * np.cos(omega * t)]


x0_1 = [0.0, 1.0]  # Base initial condition
dx0_1 = 0.04  # Variation for initial condition 2
dx0_2 = 0.09 # Variation for initial condition 3

x0_2 = [x0_1[0] + dx0_1, x0_1[1]+0.02]
x0_3 = [x0_1[0] + dx0_2, x0_1[1]+0.03]


t = np.linspace(0, 50, 1000)


sol_1 = odeint(duffing, x0_1, t, args=(alpha, beta, gamma, omega))
sol_2 = odeint(duffing, x0_2, t, args=(alpha, beta, gamma, omega))
sol_3 = odeint(duffing, x0_3, t, args=(alpha, beta, gamma, omega))


x_1 = sol_1[:, 0]
x_2 = sol_2[:, 0]
x_3 = sol_3[:, 0]


plt.plot(t, x_1, label='Initial Condition 1')
plt.plot(t, x_2, label='Initial Condition 2 (Slight Variation)')
plt.plot(t, x_3, label='Initial Condition 3 (Slight Variation)')
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Duffing Oscillator with Different Initial Conditions')
plt.legend()
plt.grid(True)
plt.show()
