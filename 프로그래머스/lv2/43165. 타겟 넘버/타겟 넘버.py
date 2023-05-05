def solution(numbers, target):
    answer = 0
    def fn(i, n):
        nonlocal answer
        if i == len(numbers)-1 and n == target:
            answer += 1
            return
        if i == len(numbers)-1:
            return
        fn(i+1, n+numbers[i+1])
        fn(i+1, n-numbers[i+1])
    
    fn(0, numbers[0])
    fn(0, -numbers[0])
    return answer