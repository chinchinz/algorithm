class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
                if d[num] == 3:
                    del d[num]
            else:
                d[num] = 1
        for key in d.keys():
            return key