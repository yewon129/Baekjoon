def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        box = array[commands[i][0]-1: commands[i][1]]
        box.sort()
        answer.append(box[commands[i][2]-1])
    return answer