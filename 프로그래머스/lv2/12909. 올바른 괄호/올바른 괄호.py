def solution(s):
    answer = True
    stack = []
    rear = 0
    while rear < len(s):
        if s[rear] == '(':
            stack.append('(')
            rear += 1
        elif s[rear] == ')':
            if len(stack) == 0:
                answer = False
                break
            else:
                stack.pop(-1)
                rear += 1
    if len(stack) != 0:
        answer = False
    
    return answer