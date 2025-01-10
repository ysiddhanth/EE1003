import ctypes
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.lines import Line2D  # For creating custom legend handles

# Load the shared object file
lib = ctypes.CDLL('./derivative.so')

# Call the main function in the shared library to generate values.dat
lib.main()    
# Create a mesh grid for the contour plot
xx = np.linspace(0,2,30)
yy = ((math.e)**xx)*np.cos(xx)
# Plot the contour and scatter points
plt.figure(figsize=(8, 8))
# Read the generated data file
data = np.loadtxt("values.dat", skiprows=1)  # Skip header
x, y = data[:, 0], data[:, 1]  # Separate x and y columns into arrays

# Results are stored in y and y_prime

plt.plot(xx,yy,color='blue', linestyle='dashed', label = "Theory")  # Contour plot for the equation
plt.scatter(x, y, s=1, c='red', label="Sim")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
# Add legend with proxy handles
plt.legend()
plt.savefig('fig1.png')
plt.show()

