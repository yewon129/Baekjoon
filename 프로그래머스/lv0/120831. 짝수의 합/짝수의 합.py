def solution(n):
    answer = 0
    box = n
    while box:
        if box % 2 == 0:
            answer += box
            box -= 2
        else:
            box -= 1
    return answer