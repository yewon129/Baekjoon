def solution(s):
    box = s.split(' ')
    answer = []
    
    for i in box:
        i = i.capitalize()
        answer.append(i)
    return ' '.join(answer)
