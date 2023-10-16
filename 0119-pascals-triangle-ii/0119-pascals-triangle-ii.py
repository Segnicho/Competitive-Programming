class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1], [1, 1]]
        for _ in range(1, rowIndex):
            curr = []
            upper = res[-1]
            curr.append(upper[0])
            for i in range(1, len(upper)):
                curr.append(upper[i-1] + upper[i])
            
            curr.append(upper[-1])
            res.append(curr)

        return res[rowIndex]