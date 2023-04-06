class Solution:
    def minSteps(self, n: int) -> int:

        def recur(num = n):
            for i in range(2, int(num**0.5)+1):
                if num%i == 0:
                    return recur(num/i) + i
            return num
        return int(recur()) if n != 1 else 0
    
    
                           
    
    
    
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           

    
    
    
    
    
    
        # def minSteps(self, n):
        # for i in xrange(2, int(n**0.5) + 1):
        #     if n % i == 0:
        #         return self.minSteps(n / i) + i
        # return 0 if n == 1 else n

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    