class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = list(range(1,len(nums)+1))
        for i in range(len(nums)):
            ret[nums[i]-1] = 0
        return list(filter(lambda x : x != 0, ret))