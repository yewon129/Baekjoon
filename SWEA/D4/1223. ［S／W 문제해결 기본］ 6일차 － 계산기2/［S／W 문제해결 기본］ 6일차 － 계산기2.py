T = 10
for tc in range(1, T+1):
    N = int(input())
    s = str(input())
    box = []
    i = 0
    while i < N:
        if s[i] == '*':
            num = box.pop()
            i += 1
            box.append(int(s[i])*num)
        elif s[i] == '+':
            pass
        else:
            box.append(int(s[i]))
        
        i += 1
    
    print(f'#{tc} {sum(box)}')