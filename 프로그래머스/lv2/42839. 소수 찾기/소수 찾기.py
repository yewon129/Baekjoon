from itertools import permutations

def solution(numbers):
    answer = 0
    nums = [int(i) for i in numbers]
    for i in range(2,len(numbers)+1):
        box = list(set(list(tuple(permutations(numbers, i)))))
        temp = []
        for j in box:
            n = int(''.join(j))
            temp.append(n)
        nums = nums + temp
    nums = list(set(nums))
    
    def find(n):
        if n == 1 or n==0:
            return 0
        k = 2
        while k < n:
            if n % k == 0:
                return 0
            k += 1
        return 1
    
    for n in nums:
        answer += find(n)
    
    return answer