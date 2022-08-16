N, M = map(int, input().split())
dict = {}
for i in range(1, N+1):
    a = input()
    dict[i] = a
    dict[a] = i

for j in range(M):
    x = input()
    if x.isdigit() == True:
        print(dict[int(x)])
    else:
        print(dict[x])
