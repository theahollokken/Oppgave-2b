import numpy as np
import matplotlib.pyplot as plt

# Definer løsningen av Burgers ligning
def u(x, t, nu):
    return 2 / (1 + np.exp((x - t) / nu))

# Definer parametere
x_values = np.linspace(-5, 5, 1000)
t_values = np.linspace(0, 2, 100)
nu_values = [5, 0.5, 0.3, 0.1, 0.01, 0.015, 0.0001]  # Verdier for viskositetsparameteren

# Plot løsningen for forskjellige verdier av nu
plt.figure(figsize=(12, 6))
for nu in nu_values:
    plt.plot(x_values, u(x_values, 0, nu), label=f'ν = {nu}')


plt.xlabel('x')
plt.ylabel('u(x,0)')
plt.legend()
plt.grid(True)
plt.show()