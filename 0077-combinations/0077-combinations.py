class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def rec(i=1, temp=[]):
            size = len(temp)
            if i > n+1 or size > k:
                return
            if size == k:
                res.append(temp[:])
                return
            temp.append(i)
            rec(i+1, temp)
            temp.pop()
            rec(i+1, temp)
        rec()
        return res