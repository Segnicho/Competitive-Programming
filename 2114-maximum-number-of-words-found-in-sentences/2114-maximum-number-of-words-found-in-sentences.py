class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(sentence.split()) for sentence in sentences])
        # mx = -1
        # for sentence in sentences:
        #     arr = sentence.split()
        #     mx = max(mx, len(arr))
        # return mx
    