class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount = Counter(p)
        scount = Counter(s[:len(p)])
        res = []
        if pcount == scount:
            res.append(0)
        psize = len(p)
        ssize = len(s)
        for i in range(psize, ssize):
            scount[s[i]] = scount.get(s[i], 0) + 1
            scount[s[i-psize]]-= 1
            if pcount == scount:
                res.append(i-psize+1)
        return res
        