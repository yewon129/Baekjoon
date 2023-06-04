n = int(input())

lst = []
for _ in range(n):
    name, e = map(str, input().split())
    if e == 'enter':
        lst.append(name)
    elif e == 'leave':
        lst.remove(name)

lst.sort(reverse=True)
for name in lst:
    print(name)