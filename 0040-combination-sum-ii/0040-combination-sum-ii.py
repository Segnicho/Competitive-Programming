class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTracking(i, temp, sm):
            if sm == target:
                res.append(temp[:])
                return
            ans = set()
            for index in range(i, len(candidates)): 
                if candidates[index] not in ans:
                    ans.add(candidates[index])
                    if sm + candidates[index] > target :
                        break
                    temp.append(candidates[index])
                    sm += candidates[index]
                    backTracking(index+1, temp, sm)
                    x = temp.pop()
                    sm -= x
        candidates.sort()
        backTracking(0, [] , 0)
        return res