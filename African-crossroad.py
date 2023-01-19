def main():
    arr = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]
    grid = []
    res = ""
    for _ in range(n):
        array = []
        temp = input()
        for j in range(m):
            array.append(temp[j])
        grid.append(array)

    def checkIn(board, i, j):
        directions = [[1,0], [0, 1],[-1,0],[0,-1]]
        for x, y in directions:
            k = x+i
            l = y+j
            while 0<=k<n and 0<=l<m:
                if board[k][l] == board[i][j]:
                    return False
                k+=x
                l+=y
        return True
    for i in range(n):
        for j in range(m):
            if checkIn(grid, i, j):
                res+=grid[i][j]
    print(res)
if __name__ == "__main__":
    main()
