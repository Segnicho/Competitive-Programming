class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        for i in range(n):
            maxIdx = i
            for j in range(i, n):
                if heights[j] > heights[maxIdx]:
                    maxIdx = j
            names[i], names[maxIdx] = names[maxIdx], names[i] 
            heights[i], heights[maxIdx] = heights[maxIdx], heights[i] 
        return names
                    