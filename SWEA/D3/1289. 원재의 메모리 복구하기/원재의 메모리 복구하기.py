T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input()))
    N = len(lst)
    box = [0] * N
    cnt = 0
    for i in range(N):
        if lst[i] != box[i]:
            cnt += 1
            for j in range(i, N):
                box[j] = lst[i]

    print(f'#{tc} {cnt}')