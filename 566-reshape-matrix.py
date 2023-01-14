class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(mat)*len(mat[0]))  != r*c :
            return mat
        matrix = []
        cnt = 0
        temp = []
        for row in mat:
            for col in row:
                temp.append(col)
                cnt+=1
                if cnt == c:
                    matrix.append(temp)
                    temp = []
                    cnt = 0
        return matrix
        
