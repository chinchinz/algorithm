class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        h = len(grid)
        w = len(grid[0]) if h > 0 else 0
        isVisited = [[False] * w for _ in range(h)]
        dy = [-1,1,0,0]
        dx = [0,0,-1,1]
        nIsland = 0
        
        def dfs(i, j, isVisited):
            for k in range(4):
                nI = dy[k] + i
                nJ = dx[k] + j
                if nI < 0 or nJ < 0 or nI == len(grid) or nJ == len(grid[0]): continue
                if isVisited[nI][nJ] : continue
                if grid[nI][nJ] == '0': continue
                isVisited[nI][nJ] = True
                dfs(nI, nJ, isVisited)
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '0': continue
                if isVisited[i][j]: continue
                nIsland += 1
                isVisited[i][j] = True
                dfs(i, j, isVisited)
        
        print(isVisited)
        return nIsland