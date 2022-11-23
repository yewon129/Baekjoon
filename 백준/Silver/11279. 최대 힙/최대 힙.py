import sys
import heapq

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n > 0:
        heapq.heappush(lst, -n)
    else:
        if lst:
            print(-heapq.heappop(lst))
        else:
            print(0)