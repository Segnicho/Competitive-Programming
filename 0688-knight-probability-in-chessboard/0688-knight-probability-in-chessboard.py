class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

        @cache
        def calc_probability(r, c, k):
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if k == 0:
                return 1
            return sum(calc_probability(r + x, c + y, k - 1) for x, y in moves) / 8
        
        return calc_probability(row, column, k)