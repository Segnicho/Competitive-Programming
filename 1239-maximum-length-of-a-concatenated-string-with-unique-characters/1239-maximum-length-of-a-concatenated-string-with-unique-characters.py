class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0

        def backtrack(start, string):
            nonlocal res
            if len(set(string)) != len(string):
                return

            res = max(res, len(string))

            for i in range(start, len(arr)):
                backtrack(i + 1, string + arr[i])

        backtrack(0, '')
        return res