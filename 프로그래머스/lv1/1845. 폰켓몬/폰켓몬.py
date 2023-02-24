def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n-r)) 

def solution(nums):
    answer = 0
    cnt = len(nums) // 2
    numbers = list(set(nums))
    if cnt > len(numbers):
        answer = len(numbers)
    else:
        answer = cnt
    
    return answer