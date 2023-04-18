def solution(k, tangerine):
    answer = 0
    t = dict()
    for i in range(len(tangerine)):
        if tangerine[i] not in t.keys():
            t[tangerine[i]] = 1
        else:
            t[tangerine[i]] += 1
    t = sorted(t.items(), key = lambda item: item[1], reverse=True)
    for i in range(len(t)):
        k -= t[i][1]
        answer += 1
        if k <= 0:
            break
    
    return answer