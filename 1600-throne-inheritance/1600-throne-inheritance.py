class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.throne = defaultdict(list)
        self.dead = defaultdict(list)
        
    def birth(self, parentName: str, childName: str) -> None:
        self.throne[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead[name] = True
    def getInheritanceOrder(self) -> List[str]:
        visited = set()
        currOrder = []
        if not  self.dead[self.king]: currOrder.append(self.king)
        def Successor(king, currOrder):
            if king in visited:
                return 
            visited.add(king)
            for child in self.throne[king]:
                if not self.dead[child]:
                    currOrder.append(child)
                Successor(child, currOrder)
            return currOrder
        return Successor(self.king, currOrder)
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()