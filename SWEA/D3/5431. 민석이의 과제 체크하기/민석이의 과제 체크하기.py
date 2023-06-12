T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    people = [0] * (N+1)
    for i in lst:
        people[i] = 1
    print(f'#{tc}', end=' ')
    for j in range(1, N+1):
        if people[j] == 0:
            print(j, end=' ')
    print()