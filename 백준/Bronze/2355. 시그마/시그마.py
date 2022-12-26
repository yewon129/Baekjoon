n, m = map(int, input().split())
A = min(n, m)
B = max(n, m)
cnt = 0
if (B-A) % 2 == 1:
  cnt = (A+B) * ((B-A)//2 + 1)
else:
  cnt = (A+B) * (B-A)//2 + (A+B)//2

print(cnt)