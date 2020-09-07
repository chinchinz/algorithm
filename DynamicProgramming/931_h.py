class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        r, c = len(A), len(A[0])
        
        for i in range(1, r):
            for j in range(c):
                l = A[i-1][j-1] if j-1 > -1 else 101
                r = A[i-1][j+1] if j+1 < c else 101
                u = A[i-1][j]
                A[i][j] += min(l,r,u)
        
        return min(A[-1])