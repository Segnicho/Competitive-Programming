class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        q = deque()

        prefSum = [0, nums[0]]
        
        for i in range(1, len(nums)):
            prefSum.append(nums[i]+prefSum [i])

        res = len(prefSum) + 1
        for i, num in enumerate(prefSum):
            
            while q and num < prefSum[q[-1]]:
                q.pop()            
            while q and num - prefSum[q[0]] >= k:
                res = min(res,i - q.popleft())
            q.append(i)
        return  -1 if res == len(prefSum) + 1 else res