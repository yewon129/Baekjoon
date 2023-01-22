from collections import deque


N, M =map(int, input().split())
dq = deque([i for i in range(1, N+1)])
lst = list(map(int, input().split()))
cnt = 0

for i in lst:
  while 1:
    if dq[0] == i:
      dq.popleft()
      break
    else:
      if dq.index(i) < len(dq)/2:
        while dq[0] != i:
          dq.append(dq.popleft())
          cnt += 1
      else:
        while dq[0] != i:
          dq.appendleft(dq.pop())
          cnt += 1

print(cnt)