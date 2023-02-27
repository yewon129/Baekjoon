N = int(input())

for number in range(1, N+1):
    lst = []
    cnt = 0
    answer = number
    while answer != 0:
        lst.append(answer % 10)
        answer = answer // 10
    for num in lst:
        if num == 3 or num == 6 or num == 9:
            cnt += 1

    if cnt != 0:
        print('-'*cnt, end=' ')
    else:
        print(number, end=' ')