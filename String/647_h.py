# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         dp = [[0]*n for _ in range(n)]
        
#         res = 0
#         for i in range(n-1, -1, -1):
#             for j in range(i, n):
#                 dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
#                 res += dp[i][j]
#         return res

class Solution:
    def countSubstrings(self, s):
        n = len(s)
        res = 0
        for i in range(2*n - 1):
            
            l = i//2
            r = (i+1)//2
            # print(i,l,r)
            while l >= 0 and r < n and s[l] == s[r]:
                r += 1
                l -= 1
                res += 1
        return res