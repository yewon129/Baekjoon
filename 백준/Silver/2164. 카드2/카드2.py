import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque([i for i in range(1, N+1)])

while len(arr) > 1:
    arr.popleft()
    k = arr.popleft()
    arr.append(k)

print(arr[0])