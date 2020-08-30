class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 1
        cur = nums[0]
        while i < len(nums):
            if nums[i] == cur:
                del nums[i]
            else:
                cur = nums[i]
                i+=1