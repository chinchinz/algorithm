class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i-1] if dp[i-1] > 0 else 0)
        
        print(dp)
        return max(dp)