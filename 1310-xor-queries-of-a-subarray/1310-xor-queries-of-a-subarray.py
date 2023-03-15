class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefSum = [arr[0]]
        for i in range(1, len(arr)):
            prefSum.append(prefSum[i-1] ^ arr[i])
        res = []
        print(prefSum)
        for l, r in queries:
            if l == 0:
                res.append(prefSum[r])
            else:
                res.append(prefSum[r] ^ prefSum[l-1])
        return res
        