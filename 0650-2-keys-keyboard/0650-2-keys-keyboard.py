class Solution:
    def minSteps(self, n: int) -> int:

        def recur(num = n):
            for i in range(2, int(num**0.5)+1):
                if num%i == 0:
                    return recur(num/i) + i
            return num
        return int(recur()) if n != 1 else 0
