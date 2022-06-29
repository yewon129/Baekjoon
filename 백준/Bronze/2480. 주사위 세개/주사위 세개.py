a, b, c = map(int, input().split())

ans = 0
if a != b and a != c and b != c:
    ans = max(a, b, c) * 100
elif a == b:
    if a == c:
        ans = a * 1000 + 10000
    else:
        ans = 1000 + a*100
elif b == c:
    ans = 1000 + b*100
elif a == c:
    ans = 1000 + a*100

print(ans)