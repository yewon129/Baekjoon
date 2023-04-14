def solution(numbers):
    answer = ''
    numbers.sort(key=lambda x: str(x)*3, reverse=True)
    if numbers[0] == 0:
        return '0'
    for num in numbers:
        answer = answer + str(num)
    return answer