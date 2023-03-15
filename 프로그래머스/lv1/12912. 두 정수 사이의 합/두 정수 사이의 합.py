def solution(a, b):
    answer = 0
    st = min(a,b)
    end = max(a,b)
    for i in range(st, end+1):
        answer += i
    return answer