class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        size = 2**n - 1
        md = size//2 +1
        if k  == md:
            return "1"
        elif k < md:
            return self.findKthBit(n-1, k)        
        else:
            return str(1 - int(self.findKthBit(n - 1, size - k + 1)))