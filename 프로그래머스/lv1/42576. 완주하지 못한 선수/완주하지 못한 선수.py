def solution(p, c):
    answer = ''
    p.sort()
    c.sort()
    for i in range(len(p)):
        if i == len(p)-1:
            answer = p[-1]
            break
        if p[i] != c[i]:
            answer = p[i]
            break
    return answer