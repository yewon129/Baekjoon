T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(9-N):
            flag = 0
            for k in range(N//2):
                if arr[i][j+k] != arr[i][j+N-k-1]:
                    flag = 1
                    break
            if flag == 0:
                cnt += 1

    for i in range(9-N):
        for j in range(8):
            flag = 0
            for k in range(N//2):
                if arr[i+k][j] != arr[i+N-k-1][j]:
                    flag = 1
                    break
            if flag == 0:
                cnt += 1

    print(f'#{tc} {cnt}')