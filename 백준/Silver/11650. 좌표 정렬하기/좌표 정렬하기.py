N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()
for i in range(N):
    print(arr[i][0], arr[i][1])