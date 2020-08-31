class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        if r == 1: return nums[0]
        if nums[0] < nums[1] : return nums[0]
        if nums[-2] < nums[-1] : return nums[-1]
        while l < r:
            mid = (l+r)//2
            # print(l, mid, r)
            if mid == 0 and nums[mid] < nums[mid+1] : return nums[mid]
            if mid == len(nums)-1 and nums[mid-1] < nums[mid] : return nums[mid]
            if nums[mid-1] < nums[mid] < nums[mid+1]: return nums[mid]
            if mid % 2 == 0:
                if nums[mid] != nums[mid+1]:
                    r = mid+1
                else:
                    l = mid
            else:
                if nums[mid] != nums[mid-1]:
                    r = mid+1
                else:
                    l = mid

#########
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = l+(r-l)//2
            if (mid % 2 == 1 and nums[mid-1] == nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid+1]):
                l = mid+1
            else:
                r = mid
        return nums[l]