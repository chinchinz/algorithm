class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # print(nums[-k:])
        # print(nums[:-k])
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
        # print(nums)