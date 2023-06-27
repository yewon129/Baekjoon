T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[1] == lst[0]:
        answer = lst[2]
    else:
        answer = lst[0]
    print(f'#{tc} {answer}')
    