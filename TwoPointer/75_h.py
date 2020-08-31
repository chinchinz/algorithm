class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroP, twoP = 0, len(nums)-1
        i = 0
        while i <= twoP:
            try:
                while nums[zeroP] == 0: zeroP += 1
                while nums[twoP] == 2: twoP -= 1
            except:
                print('error')
                return 
            # print(zeroP, twoP)
            if nums[i] == 0 and i > zeroP:
                nums[i], nums[zeroP] = nums[zeroP], nums[i]            
            elif nums[i] == 2 and i < twoP:
                nums[i], nums[twoP] = nums[twoP], nums[i]
            else:
                i += 1
            
            