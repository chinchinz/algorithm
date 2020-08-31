class Solution:
    def findComplement(self, num: int) -> int:
        i = 0
        while 2**i <= num:
            i += 1
        # print(i)
        if not i :
            return num^(2**i)
        return num^(2**i - 1)