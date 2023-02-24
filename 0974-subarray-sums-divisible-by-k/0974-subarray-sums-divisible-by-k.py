class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counter = Counter()
        counter[0] = 1
        tot = res = 0
        for num in nums:
            tot+=num
            rem = tot%k
            if rem not in counter:
                    counter[rem] = 1
            else:
                res+=counter[rem]
                counter[rem] +=1
        return res
    