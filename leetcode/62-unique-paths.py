# Time: O(n + m) Where N and M are dimensions of Matrix | Space: (n + m) DP Matrix Size depends on inputs
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_matrix = [[1 for col in range(m)] for row in range(n)]

        for row in range(1, n):
            for col in range(1, m):
                dp_matrix[row][col] = dp_matrix[row][col - 1] + dp_matrix[row - 1][col]

        return dp_matrix[-1][-1]

class Solution2:
    def uniquePaths(self, m, n):
        matrix = []

        for i in range(m):
            matrix.append([0] * n)

        for i in range(m):
            matrix[i][0] = 1

        for j in range(n):
            matrix[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
        return matrix[m - 1][n - 1]