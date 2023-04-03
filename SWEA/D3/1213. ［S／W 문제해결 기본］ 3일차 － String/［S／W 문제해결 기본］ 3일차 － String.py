for t in range(1, 11):
    tc = int(input())
    word = str(input())
    lst = str(input())

    cnt = 0
    for i in range(len(lst)-len(word)+1):
        if lst[i] == word[0]:
            n = 0
            while 1:
                if lst[i+n] == word[n]:
                    n += 1
                else:
                    break
                if n == len(word):
                    break
            if n == len(word):
                cnt += 1

    print(f'#{tc} {cnt}')