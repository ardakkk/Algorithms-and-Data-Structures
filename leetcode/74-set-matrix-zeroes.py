# Time: O(N * M) Where N and M are length and width of Matrix
# Space: O(1)
class Solution:
    def setZeroes(self, matrix):
        first_col_has_zero = False
        first_row_has_zero = False

        # Check if first col has a zero
        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # Check if first row has zero
        for j in range(0, len(matrix[0])):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # Use first row and first col as flags if rest of cells have zeros
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        # Zero out cells based on flags on first row and col
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # Zero out first col if necessary
        if first_col_has_zero:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0

        # Zero out first row if necessary
        if first_row_has_zero:
            for j in range(0, len(matrix[0])):
                matrix[0][j] = 0





