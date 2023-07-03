T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a,b,c,d,e = 0,0,0,0,0
    while n > 1:
        if n % 2 == 0:
            n //= 2
            a += 1
        if n % 3 == 0:
            n //= 3
            b += 1
        if n % 5 == 0:
            c += 1
            n //= 5
        if n % 7 == 0:
            d += 1
            n //= 7
        if n % 11 == 0:
            e += 1
            n //= 11

    print(f'#{tc} {a} {b} {c} {d} {e}')