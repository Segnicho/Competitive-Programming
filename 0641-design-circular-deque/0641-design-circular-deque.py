class MyCircularDeque:

    def __init__(self, k: int):
        self.maxSize = k
        self.size = 0
        self.nums = []

    def insertFront(self, value: int) -> bool:
        if self.size >= self.maxSize:
            return False
        self.nums.append(value)
        self.size += 1
        
        return True

    def insertLast(self, value: int) -> bool:
        if self.size >= self.maxSize:
            return False
        self.nums.insert(0, value)
        self.size += 1
        return True
    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.nums.pop()
            self.size -= 1
            return True
        return False
    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.nums.pop(0)
            self.size -= 1
            return True    
        return False

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.nums[-1]
    
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.nums[0]
    
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def isFull(self) -> bool:
        return self.size == self.maxSize
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()