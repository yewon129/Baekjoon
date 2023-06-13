T = int(input())

for tc in range(1, T+1):
    L, U, X = map(int, input().split())
    if X > U:
        print(f'#{tc} -1')
    elif L<=X<=U:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {L-X}')