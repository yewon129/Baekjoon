def solution(s):
    answer = 1
    stack = [s[0]]
    for i in range(1, len(s)):
        if len(stack) != 0 and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    
    if len(stack) != 0:
        answer = 0
    return answer