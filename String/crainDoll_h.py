def solution(board, moves):
    n = len(board[0])
    stack = []
    ans = 0
    for move in moves:
        for i in range(n):
            if board[i][move-1] == 0: continue
            cur = board[i][move-1]
            if stack and cur == stack[-1]:
                ans += 2
                stack.pop()
            else:
                stack.append(cur)
            board[i][move-1] = 0 
            break
    return ans






print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))