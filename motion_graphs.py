import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.integrate as integrate

data = {
    't': [0, 10, 15, 20],
    'v': [4, -4, 0, 2]
    }
data = pd.DataFrame(data)

# Create the scatter plot
plt.plot(data['t'], data['v'], marker='o')

# Add labels and title
plt.xlabel('t(s)')
plt.ylabel('v(m/s)')
plt.title('Particle Velocity vs Time')

# Show the plot
plt.show()

area = integrate.trapz(data['v'], data['t'])

print("Area under the curve:", area)

