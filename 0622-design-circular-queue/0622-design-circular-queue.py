class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        print(self.size, self.k, self.q, value)
        if self.size < self.k:
            self.q.append(value)
            self.size+=1
            return True
    def deQueue(self) -> bool:
        if self.q:
            self.q.pop(0)
            self.size-=1
            return True
    def Front(self) -> int:
        return self.q[0] if self.q else -1
    def Rear(self) -> int:
        return self.q[-1] if self.q else -1
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size==self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()