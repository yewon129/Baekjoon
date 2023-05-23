import math

def solution(n):
    answer = 0
    box = [2]
    if n == 2:
        return 1
    for i in range(3, n+1):
        flag = 0
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            box.append(i)
    return len(box)