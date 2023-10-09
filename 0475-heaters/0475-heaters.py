class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        heaters.sort()
        n = len(heaters)
        
        for i, house in enumerate(houses):
            left = 0
            right = n - 1
            curr = float("inf")
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] == house:
                    curr = 0
                    break
                elif heaters[mid] < house:
                    curr = min(curr, abs(house - heaters[mid]))
                    left = mid + 1
                    
                else:
                    curr = min(curr, abs(house - heaters[mid]))
                    right = mid
            curr = min(curr, abs(heaters[left] - house))
            res = max(res, curr)
                
        return res
    