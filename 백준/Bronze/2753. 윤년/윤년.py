N = int(input())

if N % 4 == 0 and N % 100 != 0:
    ans = 1
elif N % 400 == 0:
    ans = 1
else:
    ans = 0

print(ans)