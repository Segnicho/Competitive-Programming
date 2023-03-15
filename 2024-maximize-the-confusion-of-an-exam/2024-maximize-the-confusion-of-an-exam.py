class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = Counter({"F":0, "T":0})
        res = -1
        left = 0
        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            while min(count.values()) > k:
                count[answerKey[left]] -= 1
                left+=1
            print(res)
            res = max(res, right-left+1)
        return res