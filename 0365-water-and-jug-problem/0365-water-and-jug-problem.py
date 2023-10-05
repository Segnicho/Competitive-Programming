class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, target: int) -> bool:
        st = set()
        def dfs(sm):
            if sm == target:
                return True
            if sm > jug1Capacity + jug2Capacity or sm < 0 or sm in st:
                return False
            st.add(sm)
            return  dfs(sm + jug1Capacity) or \
                    dfs(sm-jug1Capacity) or \
                    dfs(sm + jug2Capacity) or \
                    dfs(sm-jug2Capacity)
        
        return dfs(0)
    