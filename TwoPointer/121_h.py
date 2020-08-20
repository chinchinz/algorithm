class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 가장 작을 때 사서 높을 때 팔면 됨 (가장 작을 때보다 나중에 있는..) X
        if len(prices) < 2 : return 0
        # 가장 작을 때를 찾으면 안됨. 가장 큰 차이를 찾아야 함.
        k = 0
        m = prices[0]
        M = 0
        for i in range(len(prices)):
            if prices[i] < m :
                m = prices[i]
                k = i
            M = prices[i] - m if prices[i] - m > M else M
            # print(i, m, M)
        
        return M