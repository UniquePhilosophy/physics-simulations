import matplotlib.pyplot as plt
import numpy as np
import scipy.constants

def grav_field(
    masses: np.ndarray,
    positions: np.ndarray,
    grid_size: int = 200,
    d: float = 1.0
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    x = np.linspace(-d, d, grid_size)
    y = np.linspace(-d, d, grid_size)
    X, Y = np.meshgrid(x, y)

    gx, gy = np.zeros_like(X), np.zeros_like(Y)

    for mass, pos in zip(masses, positions):
        dx = X - pos[0]
        dy = Y - pos[1]
        r = np.sqrt(dx**2 + dy**2)
        g = scipy.constants.G * mass / r**2
        gx -= g * dx / r  # Negate to point into the masses
        gy -= g * dy / r  # Negate to point into the masses

    magnitude = np.sqrt(gx**2 + gy**2)
    return X, Y, gx, gy, magnitude

def generate_start_points(position, num_lines, radius=0.1, rotation_angle=np.pi/16):
    angles = np.linspace(0, 2*np.pi, num_lines, endpoint=False) + rotation_angle
    points = np.array([
        position + radius * np.array([np.cos(angle), np.sin(angle)])
        for angle in angles
    ])
    return points

def plot_field(
    X: np.ndarray,
    Y: np.ndarray,
    gx: np.ndarray,
    gy: np.ndarray,
    magnitude: np.ndarray,
    masses: np.ndarray,
    positions: np.ndarray
) -> None:
    fig, ax = plt.subplots()
    
    start_points_m1 = generate_start_points(positions[0], 16)
    start_points_m2 = generate_start_points(positions[1], 4)

    start_points = np.concatenate((start_points_m1, start_points_m2), axis=0)
    
    ax.streamplot(
        X, Y, gx, gy, color=magnitude, linewidth=1, cmap='inferno', density=2,
        start_points=start_points
    )
    
    ax.set_aspect('equal')
    ax.set_title('Gravitational Field Lines')
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    
    ax.scatter(positions[:, 0], positions[:, 1], c='red', s=100, zorder=5)
    
    # Remove the tick labels from the axes
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.show()

def main() -> None:
    M1, M2 = 4, 1
    d = 1.0
    masses = np.array([M1, M2])
    positions = np.array([[-d/2, 0], [d/2, 0]])
    X, Y, gx, gy, magnitude = grav_field(masses, positions, d=d)
    plot_field(X, Y, gx, gy, magnitude, masses, positions)

if __name__ == '__main__':
    main()
