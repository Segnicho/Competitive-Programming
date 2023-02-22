class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount = Counter(p)
        scount = Counter(s[:len(p)])
        res = []
        if pcount == scount:
            res.append(0)
            
        for i in range(len(p), len(s)):
            scount[s[i]] = scount.get(s[i], 0) + 1
            scount[s[i-len(p)]]-= 1
            if pcount == scount:
                res.append(i-len(p)+1)
            if scount[s[i-len(p)]] == 0:
                       del(scount[s[i-len(p)]])
                    
        return res
        