x, y, w, h = map(int, input().split())

minV = 1000000
if (w-x) ** 2 < minV:
    minV = (w-x) ** 2
if (h-y) ** 2 < minV:
    minV = (h-y) ** 2
if (x) ** 2 < minV:
    minV = x ** 2
if y ** 2 < minV:
    minV = y ** 2

print(round(minV ** 0.5))