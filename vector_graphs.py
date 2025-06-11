import matplotlib.pyplot as plt
import numpy as np

# Define the origin point
origin = np.array([[0, 0], [0, 0], [8, 7], [0, 0]]).T  # Transpose to match shape

# Define the vectors
vectors = np.array([[8, 7], [4, -2], [4, -2], [12, 5]]).T  # Transpose to match shape

# Plot the vectors
plt.quiver(origin[0], origin[1], vectors[0], vectors[1], angles='xy', scale_units='xy', scale=1, color=['r', 'g', 'g', 'b'])
plt.xlim(0, 15)
plt.ylim(-5, 10)
plt.grid()
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')

plt.text(9, 6, 'F1', fontsize=12, color='r', ha='right') 
plt.text(5, -3, 'F2', fontsize=12, color='g', ha='right')
plt.text(13, 4, 'F3', fontsize=12, color='b', ha='right')

plt.xlabel('X-axis (*10^7 Newtons)')
plt.ylabel('Y-axis (*10^7 Newtons)')
plt.title('2D Force Vectors on an asteroid represented as a point mass at the origin')

plt.show()
