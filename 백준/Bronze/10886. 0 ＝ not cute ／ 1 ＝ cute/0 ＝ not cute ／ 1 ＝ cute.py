N = int(input())
lst = [0] * 2
for _ in range(N):
    a = int(input())
    lst[a] += 1

if lst[0] > lst[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")