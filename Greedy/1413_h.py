class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        
        m = min(nums)
        if m > 0 : return 1
        else : return abs(m) + 1