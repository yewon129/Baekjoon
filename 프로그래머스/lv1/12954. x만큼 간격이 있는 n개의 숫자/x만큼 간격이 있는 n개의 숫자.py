def solution(x, n):
    answer = [x]
    n -= 1
    num = x
    while n:
        num += x
        answer.append(num)
        n -= 1
    return answer