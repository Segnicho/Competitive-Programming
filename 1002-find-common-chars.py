class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cont = []
        offset= ord('a')
        for word in words:
            arr = [0 for i in range(26)]
            for ch in word:
                chP = ord(ch)
                arr[chP-offset] +=1
            cont.append(arr)
        res = []
        for i in range(26):
            min_ = cont[0][i]
            for j in cont:
                min_ = min(j[i], min_)
            for k in range(min_):
                ch = chr(offset+i)
                res.append(ch)
        return res

