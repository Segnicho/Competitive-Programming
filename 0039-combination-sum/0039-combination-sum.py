class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def recur(i, arr):
            if target == sum(arr):
                res.append(arr[:])
                return
            elif sum(arr) > target:
                return
            for j in range(i,  len(candidates)):
                arr.append(candidates[j])
                recur(j, arr)
                arr.pop()                
            return arr
        recur(0, [])
        return res