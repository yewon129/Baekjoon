a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

b = b1 * b2
a = a1*b2 + a2*b1

n = 2
while 1:
    if a % n == 0 and b % n == 0:
        a //= n
        b //= n
    else:
        n += 1
    if n > a or n > b:
        break

print(a, b)

