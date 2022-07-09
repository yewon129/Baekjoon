N = int(input())
lst = [int(input()) for _ in range(N)]

a = 1
ans = []
stack = []
for i in range(N):
    num = lst[i]
    while a <= num:
        stack.append(a)
        ans.append('+')
        a += 1
    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        ans = -1
        break

if ans == -1:
    print('NO')
else:
    for k in ans:
        print(k)