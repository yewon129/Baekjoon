import sys
from collections import deque
N = int(sys.stdin.readline())
ans = deque([])

for _ in range(N):
    lst = sys.stdin.readline().split()
    if lst[0] == 'push':
        ans.append(lst[1])
    elif lst[0] == 'pop':
        if not ans:
            print(-1)
        else:
            print(ans.popleft())
    elif lst[0] == 'size':
        print(len(ans))
    elif lst[0] == 'empty':
        if not ans:
            print(1)
        else:
            print(0)
    elif lst[0] == 'front':
        if not ans:
            print(-1)
        else:
            print(ans[0])
    elif lst[0] == 'back':
        if not ans:
            print(-1)
        else:
            print(ans[-1])