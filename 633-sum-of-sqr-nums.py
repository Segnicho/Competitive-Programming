class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right = int(sqrt(c))
        left = 0
        while left <= right:
            curr_val = left**2 + right**2                
            if curr_val > c:
                right-=1
            elif curr_val < c:
                left+=1
            else:
                return True
        return False
