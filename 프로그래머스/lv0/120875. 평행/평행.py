def solution(dots):
    answer = 0
    a = (dots[0][0]-dots[1][0])/(dots[0][1]-dots[1][1])
    b = (dots[2][0]-dots[3][0])/(dots[2][1]-dots[3][1])
    if a == b:
        answer = 1
    a = (dots[0][0]-dots[2][0])/(dots[0][1]-dots[2][1])
    b = (dots[1][0]-dots[3][0])/(dots[1][1]-dots[3][1])
    if a == b:
        answer = 1
    a = (dots[0][0]-dots[3][0])/(dots[0][1]-dots[3][1])
    b = (dots[1][0]-dots[2][0])/(dots[1][1]-dots[2][1])
    
    if a == b:
        answer = 1
    return answer