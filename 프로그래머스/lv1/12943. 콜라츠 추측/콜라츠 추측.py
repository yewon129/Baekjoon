def solution(num):
    cnt = 0
    if num == 1:
        return 0
    while 1:
        if cnt ==500:
            return -1
        if num == 1:
            break
        if num % 2 == 0:
            num //= 2
        else:
            num *= 3
            num += 1
        cnt += 1
    return cnt