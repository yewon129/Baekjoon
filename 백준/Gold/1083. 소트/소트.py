import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline())

for i in range(N-1):
    maxV = lst[i]
    box = 0
    if S == 0:
        break
    for j in range(i+1, N):
        x = j-i
        if lst[j] > maxV:
            maxV = lst[j]
            box = x
        if x>=S:
            break
    if box:
        S -= box
        lst.remove(maxV)
        lst.insert(i, maxV)

    if lst[i] < lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
        S -= 1


for k in lst:
    print(k, end=' ')