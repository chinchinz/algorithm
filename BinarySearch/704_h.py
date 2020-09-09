class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect_left(nums, target)
        if i > len(nums)-1 : return -1
        return i if nums[i] == target else -1