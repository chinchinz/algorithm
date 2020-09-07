class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        self.r, self.c = len(grid), len(grid[0])
        visit = [[False]*self.c for _ in range(self.r)]
        # print(visit)
        dy = [1,-1,0,0]
        dx = [0,0,1,-1]
        self.cnt = 0
        
        def dfs(y, x):
            
            for k in range(4):
                ny = dy[k] + y
                nx = dx[k] + x
                if ny<0 or nx<0 or ny==self.r or nx==self.c: continue
                if grid[ny][nx] == 0: continue
                if visit[ny][nx]: continue
                visit[ny][nx] = True
                self.cnt += 1
                dfs(ny, nx)
        for i in range(self.r):
            for j in range(self.c):
                if grid[i][j] == 0: continue
                if visit[i][j]: continue
                self.cnt = 1
                visit[i][j] = True
                dfs(i, j)
                ans = max(ans, self.cnt)
        return ans