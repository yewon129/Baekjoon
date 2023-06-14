for tc in range(1, 11):
    N = int(input())
    s = str(input())
    answer = 0
    for i in range(N):
        if s[i] == '+':
            pass
        else:
            answer += int(s[i])

    print(f'#{tc} {answer}')