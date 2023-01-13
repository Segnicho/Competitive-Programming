class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rw = [[0,1], [1,0],[-1,0],[0,-1]]
        for i, row in enumerate(matrix):
            for j,col in enumerate(row):
                if col == 0:
                    for x, y in rw:
                        si = x+i
                        sj = y+j
                        while 0<=si<m and 0<=sj<n:
                            if matrix[si][sj] ==0:
                                si+=x
                                sj+=y
                                continue
                            matrix[si][sj] = "0"
                            si+=x
                            sj+=y
        print(matrix)
        for i, row in enumerate(matrix):
            for j,col in enumerate(row):
                if col =="0":
                    matrix[i][j] = 0
        return matrix


