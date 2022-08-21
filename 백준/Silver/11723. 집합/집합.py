import sys
M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    arr = sys.stdin.readline().strip().split()
    if len(arr) == 1:
        if arr[0] == 'all':
            S = set([i for i in range(1,21)])
        else:
            S = set()
        continue

    else:
        word, x = arr[0], arr[1]
        x = int(x)
        if word == 'add':
            S.add(x)
        elif word == 'remove':
            S.discard(x)
        elif word == 'check':
            print(1 if x in S else 0)
        elif word == 'toggle':
            if x not in S:
                S.add(x)
            else:
                S.discard(x)