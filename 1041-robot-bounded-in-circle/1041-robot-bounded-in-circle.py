class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        a, b, x, y = 0, 0, 0, 1
        for i in instructions:
            if i == 'R': x, y = y, -x
            if i == 'L': x, y = -y, x
            if i == 'G': a, b = a + x, b + y
        
        return (a, b) == (0, 0) or (x, y) != (0,1)
        
    