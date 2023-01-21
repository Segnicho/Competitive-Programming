class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        mx = max(nums)
        arr = [0]*(mx+1)
        for num in nums:
            arr[num]+= 1
        tot = 1
        res = []
        for i in range(1, len(arr)):
            if i == target:
                for j in range(tot, tot+ arr[i]):
                    res.append(j-1)
                return res
            tot+=arr[i]
