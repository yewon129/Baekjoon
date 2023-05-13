def solution(s):
    answer = ''
    lst = list(map(str, s.split(" ")))
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if j % 2 == 0:
                answer = answer + lst[i][j].upper()
            else:
                answer = answer + lst[i][j].lower()
        if i != len(lst)-1:
            answer = answer + ' '
    return answer