def solution(numbers):
    N = len(numbers)
    answer = [-1] * N
    stack = []
    
    for idx, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            answer[stack.pop()] = number
        stack.append(idx)
    return answer
    