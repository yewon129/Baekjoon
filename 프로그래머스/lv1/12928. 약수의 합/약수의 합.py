def solution(n):
    answer = 0
    a = 1
    while a <= n:
        if n % a == 0:
            answer += a
        a += 1
    return answer