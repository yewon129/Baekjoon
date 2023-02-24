from itertools import permutations

# def find(num):
#     if num < 2:
#         return 0
#     for i in range(2, num):
#         if num % i == 0:
            


def solution(numbers):
    answer = 0
    nums = []
    
    for i in range(1, len(numbers)+1):
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
    
    box = list(set(map(int, set(sum(nums, [])))))
    
    for num in box:
        if num < 2:
            pass
        else:
            flag = 0
            for i in range(2, num):
                if num % i == 0:
                    flag = 1
                    break
            if flag == 0:
                answer += 1
    
    return answer