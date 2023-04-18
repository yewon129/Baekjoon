def solution(people, limit):
    answer = 0
    N = len(people)
    people.sort()
    a = 0
    b = N-1
    while 1:
        if people[a] + people[b] <= limit:
            a += 1
            b -= 1
            answer += 1
        else:
            answer += 1
            b -= 1
        if a > b:
            break
        if a >= N or b <= 0 or a == b:
            answer += 1
            break
            
    return answer