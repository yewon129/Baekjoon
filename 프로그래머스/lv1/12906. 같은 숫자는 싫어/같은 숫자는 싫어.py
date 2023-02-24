def solution(arr):
    answer = [arr[0]]
    rear = 0
    while rear < len(arr):
        i = arr[rear]
        if answer[-1] != i:
            answer.append(i)
        rear += 1
    return answer