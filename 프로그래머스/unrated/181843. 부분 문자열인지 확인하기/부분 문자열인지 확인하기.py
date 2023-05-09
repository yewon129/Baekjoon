def solution(my_string, target):
    answer = 0
    for i in range(len(my_string)-len(target)+1):
        if target == my_string[i:i+len(target)]:
            return 1
    return 0