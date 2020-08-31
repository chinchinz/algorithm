class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        dy = [-1,0,1]
        dx = [-1,0,1]
        newBoard = deepcopy(board)
        
        for i in range(r):
            for j in range(c):
                live, dead = 0, 0
                for m in range(3):
                    for n in range(3):
                        if m == 1 and n == 1: continue
                        ny = i + dy[m]
                        nx = j + dx[n]
                        if ny < 0 or nx < 0 or ny == r or nx == c: continue
                        # print(ny, nx, board[ny][nx])
                        if board[ny][nx] == 1 : live += 1
                        if board[ny][nx] == 0 : dead += 1
                if live < 2 : newBoard[i][j] = 0
                if live > 3 : newBoard[i][j] = 0
                if live == 3 : newBoard[i][j] = 1
                    
        board[:] = newBoard