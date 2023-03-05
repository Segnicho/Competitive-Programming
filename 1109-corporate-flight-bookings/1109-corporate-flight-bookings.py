class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        """
        [10,0+20+25,-10,-20,0,-25]
        [10,55,45,25, 25, 0]
        
        """
    
        res = [0]*(n+1)
        for first,last, seats in bookings:
            res[first-1] += seats
            res[last] -= seats
        
        for i in range(1, len(res)):
            res[i] += res[i-1]
        
        return res[:-1]