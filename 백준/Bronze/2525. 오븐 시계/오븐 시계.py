A, B = map(int, input().split())
C = int(input())

a = C // 60
b = B + C - (60 * a)
m = b % 60
h = (A + a + b // 60 ) % 24

print(h, m)