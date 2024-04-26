## Assignment-02 (Gauss Elimination)

### Gaussian Elimination
Gaussian elimination is a method used to solve systems of linear equations. It operates by systematically eliminating variables from the equations until a solution is found. This technique is fundamental in various fields such as mathematics, physics, engineering, and computer science.

### How Gaussian Elimination Works
Forward Elimination: The method starts by converting the system of equations into an equivalent triangular system through a series of row operations. This process simplifies the system and makes it easier to solve.
Back Substitution: Once the triangular system is obtained, the solution is found by solving for each variable one by one, starting from the bottom and working upwards.

### Explanation of Code
The provided Python code implements Gaussian elimination to solve a system of linear equations of the form (AX = B). Here's a breakdown of the code:

**gauss_elimination Function:** This function takes two parameters:
- a_matrix: Coefficient matrix (A) of the system.
- b_matrix: Right-hand side vector (B) of the system.

**Input Validation:** The function validates the dimensions of the input matrices to ensure they are compatible for Gaussian elimination.

**Forward Elimination:** The code performs forward elimination with partial pivoting to convert the coefficient matrix into an upper triangular form.

**Back Substitution:** After obtaining the upper triangular form, the code performs back substitution to find the solution vector (X).

**Printing Solution:** Finally, the code prints the solution vector (X) to the console.

### How to Use
To use this code, follow these steps:
1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python file (e.g., gaussian_elimination.py).
3. Run the Python script.
4. Enter the values for the coefficient matrix when prompted.
5. Enter the values for the constant matrix when prompted.
6. View the solution vector printed to the console.
