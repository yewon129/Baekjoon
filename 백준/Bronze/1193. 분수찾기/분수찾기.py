S = int(input())

l= 1
while S>l:
    S -= l
    l += 1

if l % 2 == 0:
    a = S
    b = l - S + 1
else:
    a = l - S + 1
    b = S

print(f'{a}/{b}')