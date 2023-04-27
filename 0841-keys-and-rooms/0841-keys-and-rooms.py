class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def bfs(node):
            q = deque([0])
            while q:
                node = q.popleft()
                visited.add(node)
                for num in rooms[node]:
                    if num not in visited:
                        q.append(num)
                        visited.add(num)
        bfs(0)
        return len(visited) == len(rooms)