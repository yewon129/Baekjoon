def solution(n):
    N = bin(n)
    cnt = 0
    for i in range(len(N)):
        if N[i] == '1':
            cnt += 1
    answer = n
    while 1:
        answer += 1
        box = bin(answer)
        c = 0
        for i in range(len(box)):
            if box[i] == '1':
                c += 1
            if c > cnt:
                break
        if c == cnt :
            break
        
    return answer