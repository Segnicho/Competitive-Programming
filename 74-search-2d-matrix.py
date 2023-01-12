class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for rw in matrix:
            for col in rw:
                if col == target:
                    return True
        return False
