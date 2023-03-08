class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        def recur(k):
            if  k == 1:
                return 0
            elif k%2 == 0:
                return 1 - recur(math.ceil(k/2))
            return recur(math.ceil(k/2))
        return recur(k)
    