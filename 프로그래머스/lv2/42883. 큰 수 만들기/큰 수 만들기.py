def solution(number, k):
    N = len(number)
    stack = [number[0]]
    
    for i in range(1,N):
        if len(stack) == 0:
            stack.append(number[i])
        else:
            if number[i] > stack[-1]:
                if k > 0:
                    while k:
                        if len(stack) == 0:
                            break
                            
                        if stack[-1] < number[i]:
                            stack.pop()
                            k -= 1
                        else:
                            break
            stack.append(number[i])
    
    if k != 0:
        while k:
            stack.pop()
            k -= 1
    answer = ''.join(stack)
    
    return answer