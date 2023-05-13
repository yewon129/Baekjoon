def solution(n):
    answer = 0
    temp = ''

    while n:
        temp = temp + str(n%3)
        n = n // 3
        if n == 0:
            break
        if n < 3:
            temp = temp + str(n)
            break
    
    k = 0
    for i in range(len(temp)-1, -1, -1):
        answer += int(temp[i]) * (3**k)
        k += 1
        
    return answer