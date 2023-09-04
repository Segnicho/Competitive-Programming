class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left , right = 0, num
        
        while left <= right:
            md = (left + right)//2
            curr = md * md
            if  curr == num:
                return True
            elif curr < num:
                left = md + 1
            else:
                right = md -1
                
        return False