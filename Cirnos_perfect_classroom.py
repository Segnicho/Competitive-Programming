
def solve():
    num =  int(input())
    y = num & (~num +1)
    while num == y or y&num == 0:
        y+=1
    return y
def main():
    tcs = int(input())
    for _ in range(tcs):
        print(solve())
main()
