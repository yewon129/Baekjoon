def solution(priorities, location):
    answer = 0
    box = [[priorities[i], i] for i in range(len(priorities))]
    while box:
        flag = 0
        for i in range(1, len(box)):
            if box[0][0] < box[i][0]:
                a = box.pop(0)
                box.append(a)
                flag = 1
                break
        if flag == 0:
            if box[0][1] != location:
                answer += 1
                box.pop(0)
            else:
                answer += 1
                break
    return answer