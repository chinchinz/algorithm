class Solution:
    def maxPower(self, s: str) -> int:
        ans = 1
        i = 0
        cur = 1
        while i < len(s)-1:
            if s[i] == s[i+1]:
                cur += 1
            else :
                ans = max(ans, cur)
                cur = 1
            i += 1
        ans = max(ans, cur)
        
        return ans