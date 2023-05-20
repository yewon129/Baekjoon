def solution(s):
    words = {'zero': '0', 'one':'1', 'two': '2', 'three':'3', 'four':'4', 'five': '5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    numbers = list(words.keys())
    for key, value in words.items():
        s = s.replace(key, value)
    answer = int(s)
    # def find_s(i):
    #     for num in numbers:
    #         if s[i] == num[0]:
    #             flag = 0
    #             for j in range(len(num)):
    #                 if s[i+j] != num[j]:
    #                     flag = 1
    #             if flag == 0:
    #                 return [words[num], i+len(num)]
    # i = 0
    # while i < len(s):
    #     if s[i] in ['1', '2', '3', '4','5','6','7','8','9']:
    #         answer = answer + s[i]
    #         i += 1
    #     else:
    #         box = find_s(i)
    #         i = box[1]
    #         answer = answer + box[0]
    return answer