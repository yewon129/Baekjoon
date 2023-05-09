def solution(s):
    answer = ''
    N = len(s)
    if N % 2 == 1:
        answer = s[N//2]
    else:
        answer = s[N//2-1:N//2+1]
    return answer