def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # 6 5 3 1 0
    for i in range(citations[0], -1, -1):
        h = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                h += 1
            else:
                break
        if h > i:
            break
        if answer < h:
            answer = h
    return answer