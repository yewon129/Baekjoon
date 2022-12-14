A, B = map(int, input().split())

cnt = 1
while B > A:
    if B%10 == 1:
        cnt += 1
        B //= 10
    elif B % 2 == 0:
        cnt += 1
        B //= 2
    else:
        cnt = -1
        break

if B != A:
    cnt = -1
print(cnt)