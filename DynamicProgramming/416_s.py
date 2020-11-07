class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = s // 2
        
#         dp = [[0 for a in range(s+1)] for b in range(len(nums) + 1)]
#         dp[0][0] = 1
#         for y in range(1, len(dp)):
#             cur = nums[y-1]
#             for x in range(len(dp[0])):
#                 if x < cur:
#                     dp[y][x] = dp[y-1][x]
#                 else:
#                     dp[y][x] = dp[y-1][x-cur] or dp[y-1][x]
                    
#         return dp[len(nums)][s]


        dp = [0 for a in range(s+1)]
        dp[0] = 1
        
        for y in range(1, len(nums)):
            cur = nums[y-1]
            for x in range(len(dp)-1, 0, -1):
                if x < cur:
                    dp[x] = dp[x]
                else:
                    dp[x] = dp[x] or dp[x-cur]
                
        return dp[-1]