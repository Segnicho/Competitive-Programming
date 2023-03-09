class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def recur(ind, temp):
            if ind >= len(cookies):
                return max(temp)
            mn = float("inf")
            if temp.count(0) > len(cookies) -ind:
                return float("inf")
            for i in range(k):
                temp[i] += cookies[ind]
                mn = min(mn, recur(ind+1, temp))
                temp[i] -= cookies[ind]
            return mn
        temp = [0]*k
        return recur(0, temp)
    
        