def set_zeroes(matrix):
    if not matrix:
        return
    
    """
    M - Number of rows
    N - Number of columns
    """
    M, N = len(matrix), len(matrix[0])

    # check if the first row has a zero element
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(N))

    # check if the first column has a zero element
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(M))

    # use first row and first column to mark zeros
    for i in range(0, M):
        for j in range(0, N):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # zero out cells based on marks
    for i in range(0, M):
        for j in range(0, N):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # zero out the first row if needed
    if first_row_has_zero:
        for j in range(N):
            matrix[0][j] = 0

    # zero out the first column if needed
    if first_col_has_zero:
        for i in range(M):
            matrix[i][0] = 0

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 0, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

set_zeroes(matrix)
for row in matrix:
    print(row)
