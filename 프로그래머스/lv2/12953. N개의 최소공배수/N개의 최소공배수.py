def solution(arr):
    answer = 0
    n = max(arr)
    while 1:
        flag = 0
        for i in arr:
            if n % i != 0:
                flag = 1
                break
        if flag == 0:
            break
        n += 1
    return n