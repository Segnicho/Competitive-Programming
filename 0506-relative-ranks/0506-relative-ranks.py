class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans = [0]*len(score)
        nscore = []
        counter = Counter()
        for i, num in enumerate(score):
            nscore.append(-num)
            counter[num] = i
        heapq.heapify(nscore)
        for i in range(len(score)):
            nnum = -heapq.heappop(nscore)
            if i == 0:
                ans[counter[nnum]] = ("Gold Medal")
            elif i == 1:
                ans[counter[nnum]] = ("Silver Medal")
            elif i == 2:
                ans[counter[nnum]] = ("Bronze Medal")
            else:
                ans[counter[nnum]] = str(i+1)
        return ans