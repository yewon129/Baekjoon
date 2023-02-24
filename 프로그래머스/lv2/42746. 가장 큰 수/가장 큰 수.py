def solution(numbers):
    answer = ''
    numbers.sort(reverse=True, key=lambda x : str(x)*3)
    if numbers[0] == 0:
        answer = "0"
    else:
        answer = "".join(str(i) for i in numbers)
    return answer