def solution(operations):
    answer = []
    q = []
    for i in range(len(operations)):
        temp = list(map(str, operations[i].split()))
        if temp[0] == 'I':
            q.append(int(temp[-1]))
        else:
            q.sort()
            if len(q) > 0:
                if temp[1] == '1':
                    q.pop()
                else:
                    q.pop(0)
    if len(q) == 0:
        answer = [0,0]
    else:
        answer = [max(q), min(q)]
    return answer