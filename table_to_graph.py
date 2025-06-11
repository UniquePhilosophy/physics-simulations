import matplotlib.pyplot as plt
import numpy as np

bx = [1550, 1687, 1789, 1862, 1894, 1924, 1918, 1924, 1894, 1862, 1789, 1687, 1550] # Bx(0, 0)/µT
x = [-15, -12.5, -10, -7.5, -5, -2.5, 0, 2.5, 5, 7.5, 10, 12.5, 15]  # R/cm

# Linear regression to find the line of best fit
# coefficients = np.polyfit(x, y, 1)
# poly = np.poly1d(coefficients)

# Generate x values for the line of best fit extending beyond the data points
# x_line = np.linspace(0, max(x) + 10, 100)
# bx_line = poly(x_line)

plt.figure(figsize=(10, 6))

plt.plot(x, bx, marker='o', linestyle='-', color='b', label='Data points')
# plt.plot(x_line, bx_line, linestyle='-', color='r', label='Line of best fit')

plt.title('Magnetic Field Strength vs Distance from the Center of the Coils')
plt.xlabel('Distance from the Center of the Coils R/cm')
plt.ylabel('Magnetic Field Strength Bx(r=0)/µT')
plt.grid(True)

plt.xticks(range(-20, 20, 5))
plt.yticks(range(0, 2500, 100))

plt.xlim(min(x), max(x) + 1)
plt.ylim(1600, 2000)

plt.legend()

plt.show()
