def solution(t, p):
    answer = 0
    n = len(p)
    p = int(p)
    for i in range(len(t)-n+1):
        num = int(t[i:i+n])
        if num <= p:
            answer += 1
    return answer