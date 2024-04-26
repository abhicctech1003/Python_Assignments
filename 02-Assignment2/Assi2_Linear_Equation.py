import numpy as np
 
def gauss_elimination(a_matrix, b_matrix):
    """
    Solves a system of linear equations using Gaussian elimination with partial pivoting.
 
    Parameters:
        a_matrix (numpy.ndarray): Coefficient matrix of shape (n, n).
        b_matrix (numpy.ndarray): Right-hand side vector of shape (n, 1).
 
    Returns:
        numpy.ndarray: Solution vector of shape (n, 1).
    """
    # Check if the coefficient matrix is square
    if a_matrix.shape[0] != a_matrix.shape[1]:
        print("Coefficient matrix must be square")
        return None
 
    # Check if the dimensions of the constant matrix match with the coefficient matrix
    if b_matrix.shape != (a_matrix.shape[0], 1):
        print("Dimensions of constant matrix do not match with coefficient matrix")
        return None
 
    n = len(b_matrix)
    x = np.zeros(n)
 
    # Create augmented matrix
    augmented_matrix = np.concatenate((a_matrix, b_matrix), axis=1)
 
    # Forward Elimination with Partial Pivoting
    for i in range(n):
        # Partial Pivoting: Find the row with the maximum absolute value in the current column
        max_row_index = i
        for k in range(i+1, n):
            if abs(augmented_matrix[k][i]) > abs(augmented_matrix[max_row_index][i]):
                max_row_index = k
        # Swap rows to bring the row with the maximum absolute value to the current row
        augmented_matrix[[i, max_row_index]] = augmented_matrix[[max_row_index, i]]
 
        # Check for zero pivot
        if augmented_matrix[i][i] == 0:
            print("Zero pivot encountered - Gaussian Elimination cannot proceed.")
            return None
 
        # Gaussian Elimination
        for j in range(i+1, n):
            scaling_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            augmented_matrix[j] = augmented_matrix[j] - scaling_factor * augmented_matrix[i]
 
    # Backward Substitution
    x[n-1] = augmented_matrix[n-1][n] / augmented_matrix[n-1][n-1]
    for i in range(n-2, -1, -1):
        summation = 0
        for j in range(i+1, n):
            summation += augmented_matrix[i][j] * x[j]
        x[i] = (augmented_matrix[i][n] - summation) / augmented_matrix[i][i]
 
    # Display solution
    print("Solution:")
    for i in range(n):
        print(f"x{i} = {x[i]}")
    return x
 
# Input matrix values
print("Enter values for the coefficient matrix:")
variable_matrix = []
for i in range(3):
    row = input("Enter row values separated by space: ").split()
    variable_matrix.append([float(val) for val in row])
print("Enter values for the constant matrix:")
constant_matrix = []
for i in range(3):
    row = float(input("Enter constant value: "))
    constant_matrix.append([row])
variable_matrix = np.array(variable_matrix)
constant_matrix = np.array(constant_matrix)
 
# Call the function with the input matrices
solution = gauss_elimination(variable_matrix, constant_matrix)
