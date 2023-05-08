def solution(want, number, discount):
    answer = 0
    N = len(discount)
    W = sum(number)
    box = []
    for i in range(len(number)):
        for k in range(number[i]):
            box.append(want[i])
    box.sort()
    for i in range(N-W+1):
        box_10 = discount[i:i+10]
        box_10.sort()
        if box == box_10:
            answer += 1
            
    return answer