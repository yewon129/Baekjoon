def solution(n):
    answer = 0
    x = 2
    while x:
        if n % x == 1:
            answer = x
            break
        x += 1
            
    return answer