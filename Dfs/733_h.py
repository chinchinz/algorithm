class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r = len(image)
        c = len(image[0])
        dy = [1,-1,0,0]
        dx = [0,0,1,-1]
        visit = [[False] * c for _ in range(r)]
        
        def dfs(image, visit, y, x, target, new):
            visit[y][x] = True
            image[y][x] = new
            for k in range(4):
                ny = dy[k] + y
                nx = dx[k] + x
                if 0 > ny or ny == len(image) or 0 > nx or nx == len(image[0]) : continue
                if visit[ny][nx] == True : continue
                if image[ny][nx] == target:
                    image[ny][nx] = new
                    dfs(image, visit, ny, nx, target, new)
        
        dfs(image, visit, sr, sc, image[sr][sc], newColor)
        
        return image
        