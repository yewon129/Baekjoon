def solution(n):
    answer = 0
    m = n
    while m > 1:
        box = m-1
        sumV = m
        while 0 <= sumV < n:
            sumV += box
            box -= 1
        if sumV == n:
            answer += 1
        m -= 1
    if n == 1:
        answer = 1
    return answer