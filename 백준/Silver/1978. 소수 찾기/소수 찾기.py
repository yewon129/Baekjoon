N = int(input())

lst = list(map(int, input().split()))

cnt = 0
for i in lst:
    box = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                box += 1
        if box == 0:
            cnt += 1
print(cnt)