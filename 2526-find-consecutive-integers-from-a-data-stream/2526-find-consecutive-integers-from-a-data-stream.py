class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.n = 0
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.n += 1
        else:
            
            self.n = 0
        return self.n >= self.k