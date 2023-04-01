T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()

    maxV = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = lst[i] * lst[j]
            box = str(num)
            flag = 0
            for k in range(len(box)-1):
                if int(box[k]) > int(box[k+1]):
                    flag = 1
                    break
            if flag == 0:
                if maxV < int(box):
                    maxV = int(box)

    print(f'#{tc} {maxV}')