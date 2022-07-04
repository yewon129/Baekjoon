N = int(input())
lst = [0] * N
for i in range(N):
    lst[i] = int(input())

for i in range(N-1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

for i in range(N):
    print(lst[i])