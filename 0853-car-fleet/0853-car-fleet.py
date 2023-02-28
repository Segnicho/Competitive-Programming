class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posSpeed = [(pos, spd) for pos, spd in zip(position, speed)]
        posSpeed.sort(reverse = True)
        
        res = []
        for pos, spd in posSpeed:
            t = (target - pos)/spd
            res.append(t)
            if len(res) > 1 and res[-1] <= res[-2]:
                res.pop()
        return len(res)
        
        