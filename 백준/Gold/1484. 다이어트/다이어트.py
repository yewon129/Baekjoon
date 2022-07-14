G = int(input())
# (현재 몸무게의 제곱) - (기억하고 있는 무게의 제곱)

now = 1
box = []
while 1:
    if now ** 2 - (now-1) ** 2 > G:
        break
    for i in range(now-1, 0, -1):
        if now ** 2 - i ** 2 == G:
            box.append(now)
            break
        if now ** 2 - i ** 2 > G:
            break
    now += 1

if box == []:
    print(-1)
else:
    for _ in box:
        print(_)