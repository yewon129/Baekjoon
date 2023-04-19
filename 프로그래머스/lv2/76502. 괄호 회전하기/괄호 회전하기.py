def solution(s):
    answer = 0
    if len(s) % 2 == 1:
        answer = 0
    else:
        for i in range(len(s)):
            stack = []
            flag = 0
            for j in range(len(s)):
                num = j + i
                if num >= len(s):
                    num -= len(s)
                if s[num] in ['(','[','{']:
                    stack.append(s[num])
                else:
                    if s[num] == ')':
                        if len(stack) != 0 and stack[-1] == '(':
                            stack.pop()
                        else:
                            flag = 1
                            break
                    elif s[num] == '}':
                        if len(stack) != 0 and stack[-1] == '{':
                            stack.pop()
                        else:
                            flag = 1
                            break
                    elif s[num] == ']':
                        if len(stack) != 0 and stack[-1] == '[':
                            stack.pop()
                        else:
                            flag = 1
                            break
            if flag == 0 and len(stack) == 0:
                answer += 1


    return answer