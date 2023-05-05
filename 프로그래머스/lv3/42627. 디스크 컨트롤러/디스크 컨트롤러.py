from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    heap = []
    i = 0
    now = 0
    start = -1
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            box = heappop(heap)
            start = now
            now += box[0]
            answer += now - box[1]
            i += 1
        else:
            now += 1
    return answer // len(jobs)