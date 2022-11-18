import sys
from collections import deque

def func(word, num):
    global lst
    if word == 'push_front':
        lst.appendleft(num)
    elif word == 'push_back':
        lst.append(num)
    elif word == 'pop_front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.popleft())
    elif word == 'pop_back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())
    elif word == 'size':
        print(len(lst))
    elif word == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif word == 'front':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
    elif word == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])


lst = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    arr = list(map(str, sys.stdin.readline().split()))
    if len(arr) == 2:
        arr[1] = int(arr[1])
    else:
        arr.append(0)
    func(arr[0], arr[1])