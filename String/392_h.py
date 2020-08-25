class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        for c in s:
            if c not in t:
                return False
        return True