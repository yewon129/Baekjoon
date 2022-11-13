A, B = map(int, input().split())
lst = []
for i in range(1, B+1):
    for _ in range(i):
        lst.append(i)
        if len(lst) > B:
            break
    if len(lst) > B:
        break

ans = 0
for k in range(A-1, B):
    ans += lst[k]

print(ans)