E, S, M = map(int, input().split())

a, b, c, cnt = 1, 1, 1, 1

a * 15 + E == b * 28 + S == c * 19 + M

while 1:
    if E == a and S == b and M == c:
        break
    a += 1
    b += 1
    c += 1
    cnt += 1
    if a >= 16:
        a -= 15
    if b >= 29:
        b -= 28
    if c >= 20:
        c -= 19

print(cnt)