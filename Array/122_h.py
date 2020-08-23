class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        max_profit, buy, sell = 0, -1, -1
        for i in range(0, length):
            if i+1 == length :
                max_profit += sell - buy
                continue
            if prices[i+1] > prices[i]:
                sell = prices[i+1]
                if buy == -1 :
                    buy = prices[i]
            else:
                max_profit += sell - buy
                sell = -1
                buy = -1
        return max_profit