N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]


count = 0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if A[x][y] == 1:
                        A[x][y] = 0
                    else:
                        A[x][y] = 1
            count += 1

flag = 1
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            flag = 0

if flag == 1:
    print(count)
else:
    print(-1)