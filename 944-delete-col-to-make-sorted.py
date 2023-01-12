class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ls = [list(row) for row in zip(*strs)]
        cnt = 0
        for words in ls:
            for i in range(len(words)-1):
                if ord(words[i]) >  ord(words[i+1]):
                    cnt+=1
                    break
        return cnt

