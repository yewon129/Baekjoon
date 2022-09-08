s = 0
for _ in range(5):
    n = int(input())
    if n >= 40:
        s += n
    else:
        s += 40

print(s // 5)