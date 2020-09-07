class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        div = 1
        while div:
            div, mod = divmod(numBottles, numExchange)
            # print(div, mod)
            ans += div
            numBottles = div + mod
        
        return ans