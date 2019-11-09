# Time: O(n + m) Where N and M are dimensions of Matrix | Space: (n + m) DP Matrix Size depends on inputs
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp_matrix = [[1 for col in range(m)] for row in range(n)]

        for row in range(1, n):
            for col in range(1, m):
                dp_matrix[row][col] = dp_matrix[row][col - 1] + dp_matrix[row - 1][col]

        return dp_matrix[-1][-1]
