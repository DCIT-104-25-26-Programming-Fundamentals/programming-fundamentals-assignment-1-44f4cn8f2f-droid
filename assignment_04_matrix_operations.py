# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
 =============================================================================
def read_matrix(rows, cols, matrix_label=""):
    matrix = []

    for i in range(rows):
        while True:
            row_text = input(f"Enter row {i + 1}{matrix_label}: ").strip().split()
            if len(row_text) != cols:
                print(f"Please enter exactly {cols} values.")
                continue

            try:
                row = [int(value) for value in row_text]
                matrix.append(row)
                break
            except ValueError:
                print("Please enter valid integer values.")

    return matrix


def transpose_matrix(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(cols):
        for j in range(rows):
            transposed[i][j] = matrix[j][i]

    return transposed


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            product_sum = 0
            for k in range(cols_a):
                product_sum += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = product_sum

    return result


def print_matrix(matrix):
    if not matrix:
        print("[]")
        return

    cols = len(matrix[0])
    widths = [0 for _ in range(cols)]

    for row in matrix:
        for j in range(cols):
            value_length = len(str(row[j]))
            if value_length > widths[j]:
                widths[j] = value_length

    for row in matrix:
        line = ""
        for j in range(cols):
            line += str(row[j]).rjust(widths[j])
            if j < cols - 1:
                line += " "
        print(line)


def main():
    # Part A — Transpose a Matrix
    print("PART A — Transpose a Matrix")
    rows_a = int(input("Enter number of rows: "))
    cols_a = int(input("Enter number of columns: "))
    matrix_a = read_matrix(rows_a, cols_a)

    print("\nOriginal Matrix:")
    print_matrix(matrix_a)

    transposed = transpose_matrix(matrix_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    # Part B — Add Two Matrices
    print("\nPART B — Add Two Matrices")
    rows_b = int(input("Enter number of rows: "))
    cols_b = int(input("Enter number of columns: "))

    matrix_b1 = read_matrix(rows_b, cols_b, " for matrix 1")
    matrix_b2 = read_matrix(rows_b, cols_b, " for matrix 2")

    added = add_matrices(matrix_b1, matrix_b2)
    print("\nSum of the matrices:")
    print_matrix(added)

    # Part C — Multiply Two Matrices
    print("\nPART C — Multiply Two Matrices")
    rows_c1 = int(input("Enter number of rows for matrix A: "))
    cols_c1 = int(input("Enter number of columns for matrix A: "))
    rows_c2 = int(input("Enter number of rows for matrix B: "))
    cols_c2 = int(input("Enter number of columns for matrix B: "))

    matrix_c1 = read_matrix(rows_c1, cols_c1, " for matrix A")
    matrix_c2 = read_matrix(rows_c2, cols_c2, " for matrix B")

    if cols_c1 != rows_c2:
        print("\nError: Number of columns in matrix A must equal number of rows in matrix B.")
        return

    product = multiply_matrices(matrix_c1, matrix_c2)
    print("\nProduct of matrix A and matrix B:")
    print_matrix(product)


if __name__ == "__main__":
    main()
