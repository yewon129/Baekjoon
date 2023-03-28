def solution(n, words):
    answer = []
    N = len(words)
    flag = 0
    person = 0
    turn = 0
    for i in range(N-1):
        if words[i][-1] == words[i+1][0]:
            box = words[0:i+1]
            if words[i+1] in box:
                flag = 1
                if (i+2) % n == 0:
                    person = n
                    turn = (i+2) // n
                else:
                    person = (i+2) % n
                    turn = (i+2) // n + 1
                break
        else:
            flag = 1
            if (i+2) % n == 0:
                person = n
                turn = (i+2) // n
            else:
                person = (i+2) % n
                turn = (i+2) // n + 1
            break
    if flag == 0:
        person = 0
        turn = 0
        
    answer = [person, turn]
    return answer