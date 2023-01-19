class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        arr = nums[:]
        for num in nums:
            num = str(num)
            r = [n for n in num]
            while r[-1] =="0":
                r.pop()
            r.reverse()
            i = ''.join(r)
            arr.append(int(i))
        count = Counter(arr)
        return len(count)
        
