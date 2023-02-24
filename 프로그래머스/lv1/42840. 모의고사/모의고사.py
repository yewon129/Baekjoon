def solution(answers):
    answer = []
    N = len(answers)
    fir = 0
    sec = 0
    thir = 0
    for i in range(1, N+1):
        ans = answers[i-1]
        if i % 5 == 0:
            if answers[i-1] == 5:
                fir += 1
        else:
            if answers[i-1] == i%5:
                fir += 1
        if i % 2 == 1:
            if ans == 2:
                sec += 1
        else:
            if (i // 2) % 4 == 1:
                if ans == 1:
                    sec += 1
            elif (i//2) % 4 == 0:
                if ans == 5:
                    sec += 1
            else:
                if ans == (i//2) % 4 + 1:
                    sec +=1
        ten = i % 10
        if ten == 1 or ten == 2:
            if ans == 3:
                thir += 1
        elif ten == 3 or ten == 4:
            if ans == 1:
                thir += 1

        elif ten == 5 or ten == 6:
            if ans == 2:
                thir += 1
        elif ten == 7 or ten == 8:
            if ans == 4:
                thir += 1
        elif ten == 9 or ten == 0:
            if ans == 5:
                thir += 1
    maxV = max(fir, sec, thir)
    if fir == maxV:
        answer.append(1)
    if sec == maxV:
        answer.append(2)

    if thir == maxV:
        answer.append(3)
    
    return answer