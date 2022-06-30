n = str(input())
if len(n) == 1:
    n = '0' + n
cnt = 0
new = n
while 1:
    box = 0
    for i in range(len(new)):
        box += int(new[i])
    box = str(box)
    new = new[-1] + box[-1]
    cnt += 1
    if new == n:
        break

print(cnt)