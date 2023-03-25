def solution(arr):
    answer = [0] * len(arr)
    for i in range(len(arr)):
        answer[i] = arr[i]
    arr.sort(reverse=True)
    if len(arr) == 1:
        answer = [-1]
    else:
        idx = answer.index(arr[-1])
        answer.pop(idx)
    return answer