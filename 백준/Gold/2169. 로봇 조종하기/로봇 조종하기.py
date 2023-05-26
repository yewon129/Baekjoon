from collections import deque

N, M =map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, M):
    arr[0][i] += arr[0][i-1]

for i in range(1, N):
    lr = arr[i][:]
    rl = arr[i][:]

    for j in range(M):
        if j == 0:
            lr[j] += arr[i-1][j]
        else:
            lr[j] += max(arr[i-1][j], lr[j-1])
    for j in range(M-1, -1, -1):
        if j == M-1:
            rl[j] += arr[i-1][j]
        else:
            rl[j] += max(arr[i-1][j], rl[j+1])
    
    for j in range(M):
        arr[i][j] = max(lr[j], rl[j])

print(arr[N-1][M-1])