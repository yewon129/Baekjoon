N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]

minV = 100000000000
for i in range(N-7):
    for j in range(M-7):
        B_cnt = 0
        W_cnt = 0
        for x in range(8):
            for y in range(8):
                if (x+y) % 2 == 1 and arr[i+x][j+y] == 'W':
                    W_cnt += 1
                if (x+y) % 2 == 1 and arr[i+x][j+y] == 'B':
                    B_cnt += 1
                if (x+y) % 2 == 0 and arr[i+x][j+y] == 'B':
                    W_cnt += 1
                if (x+y) % 2 == 0 and arr[i+x][j+y] == 'W':
                    B_cnt += 1

        if B_cnt < minV:
            minV = B_cnt
        if W_cnt < minV:
            minV = W_cnt

print(minV)