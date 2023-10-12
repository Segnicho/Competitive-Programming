class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.elements = defaultdict(int)
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.elements[val] += 1
        heappush(self.heap, val)
    def pop(self) -> None:

        self.elements[self.stack[-1]] -= 1
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        
        if self.elements[self.heap[0]] > 0:
            return self.heap[0]
        else:
            while self.elements[self.heap[0]] <= 0:
                heappop(self.heap)
            return self.heap[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()