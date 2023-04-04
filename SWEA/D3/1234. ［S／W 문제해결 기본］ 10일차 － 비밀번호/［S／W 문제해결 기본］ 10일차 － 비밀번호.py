for tc in range(1,11):
    N, numbers = map(str, input().split())
    N = int(N)
    while 1:
        flag = 0
        for i in range(len(numbers)-1):
            if numbers[i] == numbers[i+1]:
                flag = 1
                numbers = numbers[:i]+numbers[i+2:]
                break
        if flag == 0:
            break

    print(f'#{tc} {numbers}')