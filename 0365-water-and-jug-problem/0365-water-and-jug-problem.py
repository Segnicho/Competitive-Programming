class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, target: int) -> bool:
        q = deque([0])
        
        choices = [-jug1Capacity, jug1Capacity, -jug2Capacity, jug2Capacity]
        visited = set()
        while q:
            curr = q.popleft()
            for option in choices:
                tot = curr + option
                if tot == target:
                    return True 
                if tot not in visited and 0<tot<jug1Capacity + jug2Capacity:
                    visited.add(tot)
                    q.append(tot)
        
        return False