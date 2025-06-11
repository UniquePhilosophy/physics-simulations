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

# Parabolic approximation of probability density
def parabolic_probability_density(n, x, D):
    # Shift x to the well's left edge (0 to D)
    x_shifted = x + D/2
    # Each peak is centered at (k + 0.5)*D/n for k = 0, 1, ..., n-1
    # We'll model each lobe as a parabola that touches zero at the nodes
    density = np.zeros_like(x)
    for k in range(n):
        # Center of the k-th lobe
        center = (k + 0.5) * D / n
        # Distance from the center, scaled to make the parabola fit
        distance = np.abs(x_shifted - center) / (D/(2*n))
        # Parabolic lobe (1 - distance^2), clipped to stay positive
        lobe = np.maximum(0, 1 - distance**2)
        density += lobe
    # Normalize to match the peak height of the true probability density
    density *= (2/D)
    return density

# Set up plot
plt.figure(figsize=(10, 6), facecolor='#fff5d6')
ax = plt.gca()
ax.set_facecolor('#fff5d6')

# Infinite well boundaries
plt.axvline(-D/2, color='black')
plt.axvline(D/2, color='black')
plt.axhline(0, color='black', lw=1)

# Plot true probability density (for comparison, in red)
plt.plot(x, psi(n, x, D)**2, color='red', alpha=0.3, label='True $|\psi|^2$')

# Plot parabolic approximation (in blue)
plt.plot(x, parabolic_probability_density(n, x, D), color='blue', label=f'Parabolic approx. (n={n})')

# Axes formatting
plt.xlabel('Position x (×10⁻¹⁰ m)')
plt.ylabel(r'$|\psi(x)|^2$' + '\n' + r'(m$^{-1}$)',
           rotation=0,
           labelpad=20,
           linespacing=1.5)

# Remove scientific notation from x-axis
ax.xaxis.set_major_formatter(plt.FuncFormatter(
    lambda val, pos: f'{val/1e-10:.1f}'))

plt.title(f'Parabolic Approximation of Probability Density (n = {n})')
plt.xlim(-D/2 - 0.1*D, D/2 + 0.1*D)
plt.ylim(-0.1 * (2/D), 1.2 * (2/D))

# Remove y-axis ticks but keep label
plt.yticks([])

# Remove the scale indicator ("1e-10")
ax.xaxis.offsetText.set_visible(False)

plt.legend()
plt.tight_layout()
plt.show()