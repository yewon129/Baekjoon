def solution(arr, d):
    answer = []
    arr.sort()
    for i in arr:
        if i % d == 0:
            answer.append(i)
    if len(answer) == 0:
        answer = [-1]
    return answer