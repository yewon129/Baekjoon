X = int(input())

box = [64]
while 1:
    if sum(box) == X:
        print(len(box))
        break
    box.sort()
    a = box.pop(0)
    box.append(a//2)
    if sum(box) >= X:
        pass
    else:
        box.append(a//2)