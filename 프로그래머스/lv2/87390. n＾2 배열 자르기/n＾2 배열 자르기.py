import math

def solution(n, left, right):
    answer = []
    lst = [0] * (right-left + 1)
    for i in range(right-left + 1):
        target = i+left+1
        if target % n == 0:
            lst[i] = n
        else:
            lst[i] = max(math.ceil(target/n), target%n)
    return lst