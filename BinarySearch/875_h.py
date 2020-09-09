class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l+r) // 2
            if sum(ceil(p/m) for p in piles) > H: l = m+1
            else:  r = m
        return l