class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        
        frontMaxList = [max(row) for row in list(zip(*grid))]
        sideMaxList = [max(row) for row in grid]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += min(frontMaxList[i], sideMaxList[j]) - grid[i][j]
        
        return ans