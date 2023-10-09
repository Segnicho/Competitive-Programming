class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        
        if n == 0:
            return 0
        
        lps = [0] * n
        i, j = 1, 0
        while i < n:
            if needle[i] == needle[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        i = 0  
        j = 0  
        while i < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == n:
                    return i - n
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1
        
                    
                    
                
                

        
        
#         nrobinKarp = RobinKarp()
#         hrobinKarp = RobinKarp()
        
#         for i, c in enumerate(needle):
#             nrobinKarp.addLast(c)
        
#         for i in range(n):
#             hrobinKarp.addLast(haystack[i])
            
#         for j in range(m-n):
            
#             if hrobinKarp.hash == nrobinKarp.hash:
#                 return j
#             hrobinKarp.addLast(haystack[j+n])
#             hrobinKarp.pollFirst(haystack[j], n-1)
#         return -1 
        
        
# class RobinKarp:
#     def __init__(self):
#         self.hash = 0
#     def addLast(self, c):
#         num = ord(c)- ord("a") + 1
#         self.hash*=27
#         self.hash +=  num
        
#     def pollFirst(self, k, n):
#         num = ord(k)- ord("a") + 1
#         # print(self.hash, num)
#         self.hash -= (num * (27**(n-1)))
#         # print(self.hash, num
        
        
    
    
    
    
    
    
        # return self.hash
    
        # for i, c in enumerate(haystack):
        #     if c != needle[0]:
        #         continue
        #     k = i
        #     j = 0
        #     while j<n and k<m and  haystack[k] == needle[j]:
        #         k += 1
        #         j += 1
        #     if j == n:
        #         return i
        # return -1
    