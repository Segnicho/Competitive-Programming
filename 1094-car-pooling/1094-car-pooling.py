class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        end = float("-inf")
        
        for passengers, fromm , to in trips:
            end = max(to, end)
        arr = [0]*(end+2)
        for passenger, frm , too in trips:
            arr[frm] += passenger
            arr[too] -= passenger
        for i in range(1, len(arr)):
            arr[i]+=arr[i-1]
        for num in arr:
            if num > capacity:
                return False
        return True