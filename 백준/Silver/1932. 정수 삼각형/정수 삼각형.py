N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
if N == 1:
    print(arr[0][0])
else:
    arr[1][0] += arr[0][0]
    arr[1][1] += arr[0][0]
    for i in range(2, N):
        arr[i][0] += arr[i-1][0]
        arr[i][-1] += arr[i-1][-1]
        for j in range(1, i):
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

    print(max(arr[-1]))