class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        res = 0
        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or                                      arr[stack[-1]] >= arr[i]):
                md = stack.pop()
                right = i
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                freq = (right-md) * (md - left)
                res += (freq*arr[md])
            stack.append(i)
        return res % mod
                    
                    