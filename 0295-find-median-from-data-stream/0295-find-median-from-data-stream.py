class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heappush(self.large, num)
        if self.large and self.small and self.large[0] <= -self.small[0] :
            heappush(self.small, -heappop(self.large))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small,-heappop(self.large) )
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -heappop(self.small))
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()