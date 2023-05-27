N = int(input())
lst = list(map(int, input().split()))
M = int(input())
lst.sort()
minV = min(lst)
answer = 0
if M // 4 < minV:
    print(M//4)
    exit(0)
k = minV
while lst:
    minV = min(lst)
    if minV * N < M:
        N -= 1
        k = lst.pop(0)
        M -= minV
    else:
        minV = k
        break

if len(lst) == 0:
    print(minV)
elif len(lst) == 1 and M > lst[0]:
    print(lst[0])
else:
    print(M//N)