import numpy as np

# Get user input for two 2x2 matrices
matrix1 = []
matrix2 = []

print("Enter the elements for Matrix 1 (2x2):")
for i in range(2):
    row = [int(x) for x in input(f"Enter row {i+1} (space separated): ").split()]
    matrix1.append(row)

print("Enter the elements for Matrix 2 (2x2):")
for i in range(2):
    row = [int(x) for x in input(f"Enter row {i+1} (space separated): ").split()]
    matrix2.append(row)

# Convert to numpy arrays
matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

# Perform matrix addition and multiplication
sum_matrix = matrix1 + matrix2
product_matrix = np.dot(matrix1, matrix2)

print("Sum of matrices:")
print(sum_matrix)
print("Product of matrices:")
print(product_matrix)
