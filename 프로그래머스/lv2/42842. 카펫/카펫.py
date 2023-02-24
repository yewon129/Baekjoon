def solution(brown, yellow):
    answer = []
    box = []
    for i in range(1, yellow+1):
        if len(box) != 0 and i == box[-1][1]:
            break
        for j in range(1, yellow+1):
            if i * j == yellow:
                box.append([i,j])
                break
            if i * j > yellow:
                break
    
    for i in range(len(box)):
        cnt = box[i][0] * 2 + box[i][1] * 2 + 4
        if cnt == brown:
            
            answer = [box[i][1]+2, box[i][0]+2]
    
    return answer