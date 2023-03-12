class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        solutions = set()
        def backTracking(tiles = tiles, curr = []):
            for j in range(len(tiles)):
                curr.append(tiles[j])
                solutions.add(tuple(curr[:]))
                backTracking(tiles[:j] + tiles[j+1:], curr)
                curr.pop()
        
        backTracking()
        return len(solutions)
