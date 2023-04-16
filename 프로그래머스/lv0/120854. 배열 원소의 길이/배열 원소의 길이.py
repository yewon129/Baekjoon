def solution(strlist):
    N = len(strlist)
    answer = [0] * N
    for i in range(N):
        answer[i] = len(strlist[i])
    return answer