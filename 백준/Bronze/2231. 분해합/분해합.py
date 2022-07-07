N = int(input())

ans = 0
num = 1
while num < N:
    n = num
    lst = []
    while n > 0:
        lst.append(n % 10)
        n //= 10
    if num + sum(lst) == N:
        ans = num
        break
    num += 1

print(ans)