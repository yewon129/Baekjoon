from itertools import combinations

def solution(clothes):
    t_c = [tuple(i) for i in clothes]
    c = [list(j) for j in set(t_c)]
    kinds = dict()
    for i in range(len(clothes)):
        if str(c[i][1]) in kinds:
            kinds[c[i][1]] += 1
        else:
            kinds[c[i][1]] = 1
    lst = list(kinds.values())
    if len(lst) == 1:
        return lst[0]
    else:
        answer = 1
        for i in range(len(lst)):
            answer *= lst[i]+1
        return answer - 1