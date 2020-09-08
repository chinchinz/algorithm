class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if all(nums): return len(nums)-1
        l = r = 0
        zero = 0
        ans = 0
        for i, num in enumerate(nums):
            if num == 1:
                if zero:
                    r += 1
                else:
                    l += 1
            else:
                if zero:
                    ans = max(ans, l+r)
                    l, r = r, 0
                else:
                    zero = 1
            # print(i,num,l,r)
        return max(ans, l+r)