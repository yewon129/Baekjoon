while 1:
    lst = list(map(int, input()))
    if lst[0] == 0:
        break
    flag = 0
    n = len(lst)
    for i in range(n//2):
        if lst[i] != lst[n-i-1]:
            flag = 1
            print('no')
            break
    if flag == 0:
        print('yes')