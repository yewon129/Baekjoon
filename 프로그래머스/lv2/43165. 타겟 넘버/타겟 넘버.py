def solution(numbers, target):
    answer = 0
    
    def dfs(i, arr, numbers, target):
        nonlocal answer
        if len(arr) != len(numbers):
            dfs(i+1, arr+[numbers[i]] , numbers, target)
            dfs(i+1, arr+[-numbers[i]], numbers, target)
        if len(arr) == len(numbers):
            if sum(arr) == target:
                answer += 1
            return
    
    arr = []
    dfs(0, arr, numbers, target)
    
    return answer