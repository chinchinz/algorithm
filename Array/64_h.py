class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if i-1 > -1 and j-1 > -1 :
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i-1 > -1:
                    grid[i][j] += grid[i-1][j]
                elif j-1 > -1:
                    grid[i][j] += grid[i][j-1]
        return grid[h-1][w-1]