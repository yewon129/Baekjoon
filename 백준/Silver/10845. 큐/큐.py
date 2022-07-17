from sys import stdin

N = int(stdin.readline())
q=[]

for _ in range(N):
    arr = stdin.readline().split()

    if arr[0] == 'push':
        q.append(int(arr[1]))
    elif arr[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            a = q.pop(0)
            print(a)
    elif arr[0] == 'size':
        print(len(q))
    elif arr[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif arr[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])