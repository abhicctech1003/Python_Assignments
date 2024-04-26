import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x_val):
    """
    Perform Lagrange interpolation to estimate the value of y at a given x.

    Args:
        x (array-like): Array of data points (x-coordinates).
        y (array-like): Array of data points (y-coordinates).
        x_val (float): The value of x at which to interpolate.

    Returns:
        float: The interpolated value of y at x_val.
    """
    n = len(x)  # Number of data points
    p = 0       # Initialize the interpolated value
    for i in range(n):
        # Calculate the Lagrange basis polynomial
        term = 1
        for j in range(n):
            if i != j:
                term *= (x_val - x[j]) / (x[i] - x[j])
        # Add the contribution of each data point to the interpolated value
        p += y[i] * term
    return p

# Sample data points
temperature = np.array([0, 20, 40, 60, 80, 100])
pressure = np.array([1.000, 0.889, 0.745, 0.582, 0.412, 0.248])

# Interpolation points
temperatures_to_interpolate = np.array([10, 30, 50, 70, 90])

# Interpolate pressure at temperatures_to_interpolate
pressures_interpolated = lagrange_interpolation(temperature, pressure, temperatures_to_interpolate)

# Plot the data points and the interpolated curve
plt.plot(temperature, pressure, 'o', color='red', label='Data points')
plt.plot(temperatures_to_interpolate, pressures_interpolated, '-', color='green', label='Interpolated')
plt.xlabel('Temperature (°C)')
plt.ylabel('Pressure (atm)')
plt.title('Lagrange Interpolation for Pressure-Temperature Relationship')
plt.legend()
plt.grid(True)  # Add grid lines for better visualization
plt.show()
