def solution(p, c):
    answer = ''
    p.sort()
    c.sort()
    for i in range(len(c)):
        if p[i] != c[i]:
            return p[i]
    return p[-1]
