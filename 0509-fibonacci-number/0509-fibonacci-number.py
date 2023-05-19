class Solution:
    def fib(self, n: int) -> int:
        fseq = [0, 1, 1]
        for i in range(n-2):
            fseq.append(fseq[i+1] + fseq[i+2])
        return fseq[n]
