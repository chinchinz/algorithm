class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n != 1 :
            n = sum(int(x)**2 for x in str(n))
            if n in mem:
                return False
            else:
                mem.add(n)
        return True