import sys

N = int(sys.stdin.readline())
lst = list(int(sys.stdin.readline()) for _ in range(N))

lst.sort()
for i in lst:
    print(i)