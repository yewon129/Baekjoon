from itertools import combinations

def solution(number):
    answer = 0
    lst = list(combinations(number, 3))
    for sets in lst:
        cnt = 0
        for i in range(3):
            cnt += sets[i]
        if cnt == 0:
            answer += 1
    return answer