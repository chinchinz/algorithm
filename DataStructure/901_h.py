class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.stocks and self.stocks[-1][0] <= price:
            cnt += self.stocks.pop()[1]
        # print(price, cnt)
        self.stocks.append([price, cnt])
        return cnt
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)