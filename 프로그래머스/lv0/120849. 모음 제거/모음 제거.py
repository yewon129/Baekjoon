def solution(my_string):
    answer = ''
    lst = ['a', 'e','i','o','u']
    for a in my_string:
        if a not in lst:
            answer += a
    return answer