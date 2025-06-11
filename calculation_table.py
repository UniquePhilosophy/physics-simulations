import numpy as np
import pandas as pd

# This is a file meant to enrich data.

R_cm = [5.00, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0]  # R in cm
Bx_uT = [5650, 2830, 1880, 1410, 1130, 942, 808, 707]    # Bx(0, 0) in µT

ln_R_cm = np.log(R_cm)
ln_Bx_uT = np.log(Bx_uT)

# Create a DataFrame to display the table
data = {
    'R/cm': R_cm,
    'ln(R/cm)': ln_R_cm,
    'Bx(0, 0)/µT': Bx_uT,
    'ln(Bx(0, 0)/µT)': ln_Bx_uT
}

df = pd.DataFrame(data)

print(df)
