class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        res  = []        
        for i in range(1, len(arr)):
            arr[i] = arr[i-1] ^ arr[i]
        for l, r in queries:
            if l == 0:
                res.append(arr[r])
            else:
                res.append(arr[r] ^ arr[l-1])
        return res
        