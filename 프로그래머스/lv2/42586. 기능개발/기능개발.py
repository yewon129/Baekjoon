def solution(progresses, speeds):
    answer = []
    box = [0] * len(progresses)
    for i in range(len(progresses)):
        box[i] = (100 - progresses[i])//speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            box[i] += 1
    
    rear = 0
    while rear < len(box):
        cnt = 1
        for i in range(rear+1, len(box)):
            if box[i] <= box[rear]:
                cnt += 1
            else:
                break
        answer.append(cnt)
        rear += cnt
        
    return answer