class StockSpanner:

    def __init__(self):
        self.stocks = [[0,float("inf")]]
        self.i = 1
    def next(self, price: int) -> int:
        isGreater = False
        while self.stocks and self.stocks[-1][-1] <= price:
            isGreater = True  
            idx, pr = self.stocks.pop()
        self.stocks.append([self.i, price])
        self.i+=1
        return self.stocks[-1][0] - self.stocks[-2][0]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)