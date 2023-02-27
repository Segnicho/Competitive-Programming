class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = [0 if num%2 == 0 else 1 for num in nums]
        cnt = prefSum = 0
        counter= Counter({0:1})
        for num in res:
            
            prefSum += num
            cnt += counter.get(prefSum-k, 0)
            counter[prefSum] = counter.get(prefSum,0)+1
        del res
        return cnt