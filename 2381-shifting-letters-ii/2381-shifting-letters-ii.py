class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        res = [0]*n
        for i, j, d in shifts:
            if d == 1:
                res[i]+=1
                if j+1 < n:
                    res[j+1] -= 1
            else:
                res[i]-= 1
                if j+1 < n:
                    res[j+1] += 1
        
        for k in range(1,n):
            res[k] += res[k-1]
        
        i = 0
        st = [0]*n
        for i in range(n):
            if res[i]<0:
                res[i] %=-26 
            elif res[i]> 26:
                res[i]%=26
            curr = ord(s[i]) + res[i]
            if curr < ord('a'):
                st[i] = chr(curr+26)
            elif curr > ord('z'):
                st[i] = chr(ord(s[i]) + res[i]-26)
            else:
                st[i] = chr(curr)
        return "".join(st)