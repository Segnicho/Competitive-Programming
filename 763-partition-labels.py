class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dikt = {}
        for i, c in enumerate(s):
            dikt[c] = i
        rptr = count = 0
        res = []
        for i, c in enumerate(s):
            count +=1
            rptr = max(rptr,dikt[c])
            if rptr  == i:
                res.append(count)
                count = 0
        return res
                
