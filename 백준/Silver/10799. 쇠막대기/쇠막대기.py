lst = list(map(str, input()))

stack = []
cnt = 0
flag = 0
for i in range(len(lst)):
    if lst[i] == '(':
        stack.append('(')
        flag = 0
    else:
        stack.pop()
        if flag == 0:
            cnt += len(stack)
        else:
            cnt += 1
        flag = 1

print(cnt)