# Time: O(N*M) Where N and M as height and width of matrix.
# Space: O(1) We only modify the Input Matrix.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    self.sink(grid, row, col)
        return count

    def sink(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
            return

        grid[row][col] = "0"
        self.sink(grid, row + 1, col)
        self.sink(grid, row - 1, col)
        self.sink(grid, row, col + 1)
        self.sink(grid, row, col - 1)

class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sinkIsland(grid, r, c):
            if grid[r][c] == '1':
                grid[r][c] = '0'
            else:
                return

            if r + 1 < len(grid):
                sinkIsland(grid, r + 1, c)
            if r - 1 >= 0:
                sinkIsland(grid, r - 1, c)
            if c + 1 < len(grid[0]):
                sinkIsland(grid, r, c + 1)
            if c - 1 >= 0:
                sinkIsland(grid, r, c - 1)

        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    counter += 1
                    sinkIsland(grid, i, j)

        return counter