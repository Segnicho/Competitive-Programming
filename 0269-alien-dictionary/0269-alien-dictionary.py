class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        graph = defaultdict()
        for word in words:
            for ch in word:
                graph[ch] = set()
        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break
        visited = {}
        ans = []
        def dfs(ch):
            if ch in visited:
                return visited[ch]
            visited[ch] = True
            for neigh in graph[ch]:
                if dfs(neigh):
                    return True
            visited[ch] = False
            ans.append(ch)
        for ch in graph:
            if dfs(ch):
                return ""
        ans.reverse()
        return "".join(ans)