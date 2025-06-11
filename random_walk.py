import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define parameter combinations
steps_list = [10, 100, 1000]
walks_list = [10, 100, 1000]
step_size = 1

# Create a DataFrame to store results
results = pd.DataFrame(columns=["steps", "walks", "mean_distance", "std_distance"])

# Test all combinations
for steps in steps_list:
    for walks in walks_list:
        # Initialize arrays
        x_final = np.zeros(walks)
        y_final = np.zeros(walks)
        distances = np.zeros(walks)
        
        # Monte Carlo simulation
        for walk in range(walks):
            x, y = 0, 0  # Start at origin
            
            for step in range(steps):
                angle = 2 * np.pi * np.random.random()
                x += step_size * np.cos(angle)
                y += step_size * np.sin(angle)
            
            distances[walk] = np.sqrt(x**2 + y**2)
        
        # Store results
        mean_dist = np.mean(distances)
        std_dist = np.std(distances)
        results.loc[len(results)] = [steps, walks, mean_dist, std_dist]
        
        # Plot one example walk (for the largest combination only)
        if steps == 1000 and walks == 1000:
            plt.figure(figsize=(8, 6))
            plt.plot(x_final[0], y_final[0], 'b-', label='Single Walk')
            plt.scatter(0, 0, c='red', label='Start')
            plt.scatter(x_final[0], y_final[0], c='green', label='End')
            plt.title(f"Example 2D Random Walk (steps={steps})")
            plt.legend()
            plt.grid()
            plt.show()

# Save results to CSV
results.to_csv("random_walk_results.csv", index=False)
print("Results saved to 'random_walk_results.csv'")

# Print theoretical expectations
results["theoretical"] = np.sqrt(results["steps"])
print("\nResults Table:")
print(results[["steps", "walks", "mean_distance", "std_distance", "theoretical"]])