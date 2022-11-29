N = int(input())
lst = []
while 1:
    a = int(input())
    if a == -1:
        break
    else:
        lst.append(a)

q = []

for i in range(len(lst)):
    if lst[i] != 0 and len(q) < N:
        q.append(lst[i])
    elif lst[i] == 0:
        q.pop(0)

if len(q) == 0:
    print('empty')
else:
    for j in q:
        print(j, end=' ')