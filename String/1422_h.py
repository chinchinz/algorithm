# class Solution:
#     def maxScore(self, s: str) -> int:
#         ans = 0
#         if len(s) == 2:
#             return int(s[0] == '0') + int(s[1] == '1')
#         for i in range(1, len(s)):
#             print(i)
#             ans = max(ans, s[:i].count('0') + s[i:].count('1'))
#         return ans
    
#########################
class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 1 if s[0] == '0' else 0
        ones = s.count('1', 1)
        score = zeros+ones
        for i in range(1, len(s)-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            score = max(zeros+ones, score)
        
        return score