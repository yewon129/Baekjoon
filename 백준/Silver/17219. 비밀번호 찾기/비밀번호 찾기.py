import sys

N, M = map(int, sys.stdin.readline().split())

site = dict()
for _ in range(N):
    id, pw = map(str, sys.stdin.readline().split())
    site[id] = pw

for _ in range(M):
    a = str(sys.stdin.readline().rstrip())
    print(site[a])