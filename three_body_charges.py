import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import Normalize
import matplotlib.cm as cm

k_e = -8.988e9

class Particle:
    def __init__(self, position, velocity, mass, charge):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass
        self.charge = charge

    def update(self, force, dt):
        acceleration = force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt

def compute_force(p1, p2):
    r = p2.position - p1.position
    distance = np.linalg.norm(r) + 1e-10
    force_magnitude = k_e * p1.charge * p2.charge / distance**2
    force_direction = r / distance
    return force_magnitude * force_direction

particles = [
    Particle([0.0, 0.0], [0.2, 0.3], 1.0,  1e-6),
    Particle([0.2, 0.0], [-0.1, 0.2], 2.0, -1e-6),
    Particle([-0.2, 0.1], [0.1, -0.2], 1.5, 1e-6),
    Particle([0.1, 0.3], [-0.15, 0], 1.0, -1e-6),
    Particle([-0.3, -0.1], [0.2, 0.1], 0.8, 1e-6),
    Particle([0.3, 0.0], [-0.1, 0.2], 2.0, -1e-6),
    Particle([-0.4, 0.1], [0.1, -0.2], 1.5, 1e-6),
    Particle([-0.1, 0.3], [-0.15, 0], 1.0, -1e-6),
    Particle([0.15, -0.1], [0.2, 0.1], 0.8, 1e-6),
    Particle([0.05, -0.25], [-0.1, 0.15], 1.0, -1e-6)
]

dt = 0.01
steps = 1000

trajectories = [[] for _ in particles]

for step in range(steps):
    forces = [np.zeros(2) for _ in particles]

    for i, p_i in enumerate(particles):
        for j, p_j in enumerate(particles):
            if i != j:
                computed_force = compute_force(p_i, p_j)
                forces[i] += computed_force

    for i, p in enumerate(particles):
        p.update(forces[i], dt)
        trajectories[i].append(p.position.copy())

trajectories = [np.array(traj) for traj in trajectories]

fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_title("Charged Particle Motion")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.grid(True)

charges = np.array([p.charge for p in particles])
masses = np.array([p.mass for p in particles])
max_abs_charge = max(np.abs(charges)) + 1e-12

norm_charges = charges / max_abs_charge

cmap = cm.get_cmap("coolwarm")
colors = [cmap(0.5 + 0.5 * c) for c in norm_charges]

base_size = 200
sizes = base_size * (masses / max(masses))

initial_positions = np.zeros((len(particles), 2))
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], s=sizes, c=colors, edgecolors='k', zorder=2)
trails = [ax.plot([], [], '-', color=colors[i], alpha=0.3, zorder=1)[0] for i in range(len(particles))]

def init():
    empty_positions = np.zeros((len(particles), 2))
    scatter.set_offsets(empty_positions)
    for trail in trails:
        trail.set_data([], [])
    return [scatter] + trails


def update(frame):
    coords = np.array([trajectories[i][frame] for i in range(len(particles))])
    scatter.set_offsets(coords)

    for i, trail in enumerate(trails):
        trail.set_data(trajectories[i][:frame+1, 0], trajectories[i][:frame+1, 1])

    return [scatter] + trails

ani = animation.FuncAnimation(
    fig, update,
    frames=len(trajectories[0]),
    init_func=init,
    interval=20,
    blit=True
)

plt.show()
