from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heappush(heap, i)
    if heap[0] >= K:
        return 0
    while 1:
        if len(heap) < 2:
            return -1
        a = heappop(heap)
        b = heappop(heap)
        heappush(heap, a+(b*2))
        answer += 1
        if heap[0] >= K:
            break
    return answer