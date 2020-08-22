def solution(board):
    w = len(board[0])
    h = len(board)
    for i in range(1, h):
        for j in range(1, w):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
    return max([max(row) for row in board])**2