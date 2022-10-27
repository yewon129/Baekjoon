A, B = map(int, input().split())
a = 0
a += A // 100
A %= 100
a += A // 10 * 10
a += A % 10 * 100

b = 0
b += B//100
B %= 100
b += B//10 * 10
b += B % 10 * 100

print(max(a,b))