N = int(input())
lst = list(map(int, input().split()))

ans = [-1] * N
stack = []
for i in range(N):
    while len(stack) != 0 and lst[stack[-1]] < lst[i]:
        ans[stack.pop()] = lst[i]
    stack.append(i)

for i in range(N):
    print(ans[i], end=' ')