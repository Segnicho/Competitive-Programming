class MyHashMap:

    def __init__(self):
        self.dikt = {}

    def put(self, key: int, value: int) -> None:
        self.dikt[key] = value

    def get(self, key: int) -> int:
        return self.dikt[key] if key in self.dikt else -1

    def remove(self, key: int) -> None:
        if key in self.dikt:
            del self.dikt[key] 

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)