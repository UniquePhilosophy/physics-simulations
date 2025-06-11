import numpy as np
import matplotlib.pyplot as plt

# Parameters
D = 2e-10  # Width of the well in meters
n = 6      # Quantum number

# Position array
x = np.linspace(-D/2, D/2, 1000)

# Wavefunction (normalised)
def psi(n, x, D):
    return np.sqrt(2/D) * np.sin(n * np.pi * (x + D/2) / D)

# Set up plot
plt.figure(figsize=(10, 6), facecolor='#fff5d6')
ax = plt.gca()
ax.set_facecolor('#fff5d6')

# Infinite well boundaries
plt.axvline(-D/2, color='black')
plt.axvline(D/2, color='black')
plt.axhline(0, color='black', lw=1)

# Plot wavefunction
plt.plot(x, psi(n, x, D), color='red', label=f'$n = {n}$')

# Axes formatting
plt.xlabel('Position x (×10⁻¹⁰ m)')  # Using proper superscript minus
plt.ylabel(r'$\psi(x)$' + '\n' + r'(m$^{-1/2}$)',  # Multi-line label
           rotation=0, 
           labelpad=20,  # Extra padding
           linespacing=1.5)

# Remove scientific notation from x-axis
ax.xaxis.set_major_formatter(plt.FuncFormatter(
    lambda val, pos: f'{val/1e-10:.1f}'))  # Formats as regular numbers

plt.title(f'Wavefunction for n = {n} in Infinite Square Well')
plt.xlim(-D/2 - 0.1*D, D/2 + 0.1*D)
plt.ylim(-1.2 * np.sqrt(2/D), 1.2 * np.sqrt(2/D))

# Remove y-axis ticks but keep label
plt.yticks([])

# Remove the scale indicator ("1e-10") completely
ax.xaxis.offsetText.set_visible(False)

plt.legend()
plt.tight_layout()
plt.show()