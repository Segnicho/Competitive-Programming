class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(matrix[j][i])
            temp.reverse()
            matrix.append(temp)
        matrix.reverse()
        for i in range(n):
            matrix.pop()
        return matrix.reverse()
        
