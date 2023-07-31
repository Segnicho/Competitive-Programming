class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        
        
        def backTrack(start, path):
            if start == len(s):
                if len(path) == 4:
                    res.append(".".join(path.copy()))
                return 
            
            for i in range(start+1, len(s)+1):
                tmp  = s[start:i]
                if int(tmp) >= 0 and int(tmp) <= 255:
                    if len(tmp) > 1 and tmp[0] == "0":
                        break
                    path.append(tmp)
                else:
                    break
                backTrack(i, path)
                path.pop()
                
        res = []
        backTrack(0,[])
        return res
    