def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        k = 1
        cnt = 0
        while k <= i:
            if i % k == 0:
                cnt += 1
            k += 1

        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer