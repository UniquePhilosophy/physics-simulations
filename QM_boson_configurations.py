import matplotlib.pyplot as plt
import numpy as np

def find_configurations():
    configurations = []
    # Iterate through all possible combinations of occupation numbers for the 5 energy levels
    for n1 in range(5):
        for n2 in range(5):
            for n3 in range(5):
                for n4 in range(5):
                    for n5 in range(5):
                        if n1 + n2 + n3 + n4 + n5 == 4:
                            total_energy = n1*1 + n2*3 + n3*5 + n4*7 + n5*9
                            if total_energy == 16:
                                configurations.append((n1, n2, n3, n4, n5))
    return configurations

configurations = find_configurations()

# Plotting the configurations
energy_levels = [1, 3, 5, 7, 9]
num_configs = len(configurations)
fig, axes = plt.subplots(num_configs, 1, figsize=(8, 10), facecolor='#fff5d6')

if num_configs == 1:
    axes = [axes]

for idx, config in enumerate(configurations):
    ax = axes[idx]
    for i, (n, energy) in enumerate(zip(config, energy_levels)):
        if n > 0:
            for j in range(n):
                ax.plot(i, j, 'bo', markersize=10)
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, max(config)+0.5)
    ax.set_xticks(range(5))
    ax.set_xticklabels([f"{e}ε" for e in energy_levels])
    ax.set_yticks([])
    ax.set_title(f'Configuration {idx+1}: {config}')
    ax.grid(True, axis='x', linestyle='--', alpha=0.7)
    ax.set_facecolor('#fff5d6')

plt.tight_layout()
plt.show()