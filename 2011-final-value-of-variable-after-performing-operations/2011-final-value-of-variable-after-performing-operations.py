class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        res = 0
        for ch in operations:
            if ch  == "--X" or ch == "X--":
                res -= 1
            else:
                res += 1
        return res