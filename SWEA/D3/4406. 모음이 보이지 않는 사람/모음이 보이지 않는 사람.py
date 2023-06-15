T = int(input())
for tc in range(1, T+1):
    s = str(input())
    answer = ''
    box = ['a', 'e', 'i', 'o', 'u']
    for alp in s:
        if alp not in box:
            answer += alp

    print(f'#{tc} {answer}')