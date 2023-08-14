class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        path = [0] * n
  
        def bt(i, path):
            if i == len(requests):
                return 0 if all(b == 0 for b in path) else -10000
            src, dest = requests[i]
            new_path = path[:]
            new_path[src] -= 1
            new_path[dest] += 1

            return max(1 + bt(i + 1, new_path), bt(i + 1, path))
        
        return bt(0, path)