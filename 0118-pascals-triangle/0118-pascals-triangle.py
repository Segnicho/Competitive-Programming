class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for x in range(numRows):
            temp = []
            for y in range(0, x + 1):
                if y in (0, x):
                    temp.append(1)
                else:
                    temp.append(res[x-1][y-1] + res[x-1][y])
            res.append(temp)
        return res
    