class Solution:
    def splitString(self, s: str) -> bool:
    
        
        for i in range(1, len(s)):
            if self.backTrack(int(s[:i]), s[i:]):
                return True
    def backTrack(self, prevString, currString):
            
            if prevString == int(currString) + 1 :
                return True
            
            for i in range(1, len(currString) +1 ):
                temp = int(currString[:i])
                if temp + 1 == prevString:
                    if self.backTrack(int(temp), currString[i:]):
                        return True
            return False