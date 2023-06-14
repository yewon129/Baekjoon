T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    m = sum(lst)/N
    answer = 0
    lst.sort()
    for i in range(N):
        if lst[i] <= m:
            answer += 1
        else:
            break
    print(f'#{tc} {answer}')