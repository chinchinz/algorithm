class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        
        # print(index)
        return min(index) if index else -1