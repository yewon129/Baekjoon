for tc in range(1, 11):
    N = int(input())
    lst = list(map(str, input()))
    answer = 1
    stack = []
    for i in range(N):
        if lst[i] in ['(', '[', '{', '<']:
            stack.append(lst[i])
        elif lst[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                answer = 0
                break
        elif lst[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                answer = 0
                break
        elif lst[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                answer = 0
                break
        elif lst[i] == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                answer = 0
                break
    
    if len(stack) != 0:
        answer = 0
    
    print(f'#{tc} {answer}')