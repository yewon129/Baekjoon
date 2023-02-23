def solution(babbling):
    answer = 0
    for word in babbling:
        flag = 1
        while word:
            if word[0] == "a":
                if len(word) >= 3 and word[1] == "y" and word[2] == "a":
                    if len(word) == 3:
                        word = ""
                    else:
                        word = word[3:]
                else:
                    flag = 0
                    break
            elif word[0] == "y":
                if len(word) >= 2 and word[1] == "e":
                    if len(word) == 2:
                        word = ""
                    else:
                        word = word[2:]
                else:
                    flag = 0
                    break
            elif word[0] == "w":
                if len(word) >= 3 and word[1] == "o" and word[2] == "o":
                    if len(word) == 3:
                        word = ""
                    else:
                        word = word[3:]
                else:
                    flag = 0
                    break
            elif word[0] == "m":
                if len(word) >= 2 and word[1] == "a":
                    if len(word) == 2:
                        word = ""
                    else:
                        word = word[2:]
                else:
                    flag = 0
                    break
            else:
                flag = 0
                break    
        if flag == 1:
            answer += 1
    return answer