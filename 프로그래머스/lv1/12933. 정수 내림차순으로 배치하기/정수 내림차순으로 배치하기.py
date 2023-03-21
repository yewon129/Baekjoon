def solution(n):
    answer = 0
    lst = [int(e) for e in str(n)]
    lst.sort(reverse=True)
    answer = int(''.join(str(e) for e in lst))
    return answer