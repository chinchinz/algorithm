class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        sums = 0
        d = {}
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            cnt += d.get(sums-k, 0)
            d[sums] = d.get(sums, 0) + 1
        return cnt