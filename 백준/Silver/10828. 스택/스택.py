import sys

N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    lst = list(map(str, sys.stdin.readline().split()))
    if lst[0] == 'push':
        stack.append(int(lst[1]))
    elif lst[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif lst[0] == 'size':
        print(len(stack))
    elif lst[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif lst[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)