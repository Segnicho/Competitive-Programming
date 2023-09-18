class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i, child in enumerate(parent):
            graph[child].append(i)
        def dfs(i):
            nonlocal res
            longest, secondLongest = 0, 0
            for child in graph[i]:
                val = dfs(child)
                if s[child] != s[i]:
                    if val > longest:
                        secondLongest = longest
                        longest = val
                    elif val > secondLongest:
                        secondLongest = val
            res = max(res, longest + secondLongest + 1)
            return max(longest, secondLongest )+ 1
        res = 0
        dfs(0)
        return res
        