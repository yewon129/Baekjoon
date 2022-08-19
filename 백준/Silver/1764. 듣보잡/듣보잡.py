N, M = map(int, input().split())

Darr = set()
for _ in range(N):
    Darr.add(input())
    
Barr = set()
for _ in range(M):
    Barr.add(input())

box = sorted(list(Darr & Barr))

print(len(box))

for x in box:
    print(x)