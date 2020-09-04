class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dy = [1,-1,0,0]
        dx = [0,0,1,-1]
        ans = 0
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0 : continue
                
                for k in range(4):
                    ny = dy[k] + i
                    nx = dx[k] + j

                    if ny<0 or nx<0 or ny==r or nx==c:
                        ans += 1
                        continue
                    if grid[ny][nx] == 1 : continue
                    ans += 1
        
        return ans