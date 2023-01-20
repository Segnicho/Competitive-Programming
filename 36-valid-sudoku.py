class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for rw in board:
            count = Counter(rw)
            for ky, vals in count.items():
                if ky.isnumeric() and vals > 1:
                    return False
        n = 9
        aboard  = [list(rw) for rw in zip(*board)]
        for rw in aboard:
            count = Counter(rw)
            for ky, vals in count.items():
                if ky.isnumeric() and vals > 1:
                    return False
        def checkBoard(board,ix, jx):
            arr = []
            for i in range(ix, ix+3):
                for j in range(jx, jx+3):
                    arr.append(board[i][j])
            count = Counter(arr)
            for ky, val in count.items():
                if ky.isnumeric() and val>1:
                    return False
            return True
        for i in range(3):
            for j in range(3):
                ix = i*3
                jx =j*3
                if not checkBoard(board, ix, jx):
                    return False
        return  True
