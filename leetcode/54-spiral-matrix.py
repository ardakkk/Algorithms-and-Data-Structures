# Time: (N * M) Where N and M are length and width of Matrix
# Space: (N * M)
class Solution:
    def spiralOrder(self, matrix):
        spiral_list = []

        if not matrix:
            return spiral_list

        left = 0
        bottom = len(matrix) - 1
        top = 0
        right = len(matrix[0]) - 1
        direction = "right"

        while top <= bottom and left <= right:
            if direction == "right":
                for i in range(left, right + 1):
                    spiral_list.append(matrix[top][i])
                top += 1
                direction = "bottom"
            elif direction == "bottom":
                for i in range(top, bottom + 1):
                    spiral_list.append(matrix[i][right])
                right -= 1
                direction = "left"
            elif direction == "left":
                for i in range(right, left - 1, -1):
                    spiral_list.append(matrix[bottom][i])
                bottom -= 1
                direction = "top"
            elif direction == "top":
                for i in range(bottom, top - 1, -1):
                    spiral_list.append(matrix[i][left])
                left += 1
                direction = "right"

        return spiral_list

solution = Solution()
print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

