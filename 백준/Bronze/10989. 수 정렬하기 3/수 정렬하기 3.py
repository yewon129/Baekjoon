import sys

T = int(sys.stdin.readline())

box = [0] * 10001

for i in range(T):
    num = int(sys.stdin.readline())
    box[num] += 1

for i in range(10001):
    if box[i] != 0:
        for j in range(box[i]):
            print(i)