n = int(input())
m = int(input())

k = m
print(n * (k%10))
k //= 10
print(n * (k % 10))
k //= 10
print(n * k)
print(n * m)