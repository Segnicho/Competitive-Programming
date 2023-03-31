class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        while i < num + 1:
            i = i << 1
        return num ^ (i - 1)