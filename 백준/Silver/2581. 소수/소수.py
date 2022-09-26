N = int(input())
M = int(input())

lst = []
for i in range(N, M+1):
    if i == 1:
        pass
    elif i == 2:
        lst.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                lst.append(i)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))