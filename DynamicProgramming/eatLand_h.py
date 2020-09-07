def findMax(row, k):
    res = 0
    for i, num in enumerate(row):
        if i==k : continue
        res = max(res, num)
    return res

def solution(land):
    r, c = len(land), len(land[0])
    for i in range(1, r):
        for j in range(c):
            land[i][j] += findMax(land[i-1], j)
    
    return max(land[-1])





print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))