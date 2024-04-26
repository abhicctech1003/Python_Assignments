## Assignment-01 (Interpolation and Lagrange Interpolation)

### Interpolation
Interpolation is a method in mathematics and computational science used to estimate values between known data points. It is particularly useful when we have a set of discrete data points and need to estimate the value of a function at points that lie between these data points. Interpolation is commonly used in various fields such as numerical analysis, signal processing, computer graphics, and scientific computing.

### Lagrange Interpolation
Lagrange interpolation is a polynomial interpolation method that constructs a polynomial function that passes through a given set of data points. It is named after the mathematician Joseph-Louis Lagrange.

### Lagrange Interpolation Formula
Given (n) data points ((x_i, y_i)), where (i = 0, 1, 2, ..., n-1), the Lagrange interpolation polynomial (P(x)) is given by:
\[ P(x) = \sum_{i=0}^{n-1} y_i \cdot l_i(x) \]
where (l_i(x)) are the Lagrange basis polynomials defined as:
\[ l_i(x) = \prod_{j=0, j \neq i}^{n-1} \frac{x - x_j}{x_i - x_j} \]

### Explanation of Code
The provided Python code demonstrates Lagrange interpolation to estimate pressure values at given temperature points. Here's a breakdown of the code:

**lagrange_interpolation Function:** This function implements Lagrange interpolation. It takes three parameters:
- x: Array of x-coordinates (temperature points).
- y: Array of y-coordinates (pressure points).
- x_val: Value at which interpolation is to be performed (temperature at which pressure is to be calculated).

**Data Points:** The code defines arrays temperature and pressure representing known temperature-pressure data points.

**User Input:** The user is prompted to input a list of temperatures at which pressure is to be calculated.

**Interpolation:** The Lagrange interpolation function is called with the temperature and pressure data along with the user-input temperature points.

**Plotting:** The code plots the known data points as dots and the interpolated points as a continuous line.

**Visualization:** The resulting plot visualizes the pressure-temperature relationship using Lagrange interpolation.

### How to Use
To use this code, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required libraries: numpy and matplotlib.
3. Copy the provided code into a Python file (e.g., interpolation_example.py).
4. Run the Python script.
5. Enter the temperatures at which you want to interpolate pressures when prompted.
6. View the plotted graph showing the original data points and the interpolated points.
