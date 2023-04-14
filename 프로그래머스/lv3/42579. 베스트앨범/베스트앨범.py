def solution(genres, plays):
    answer = []
    nums = dict()
    for i in range(len(genres)):
        if genres[i] not in nums:
            nums[genres[i]] = [plays[i], [plays[i],i]]
        else:
            nums[genres[i]].append([plays[i],i])
            nums[genres[i]][0] += plays[i]
    
    genre = list(set(genres))
    lst = [0] * len(genre)
    for g in range(len(genre)):
        lst[g] = nums[genre[g]]
    lst.sort(reverse=True)
#     for i in range(len(lst)):
        
#     lst.sort(key=lambda x: x[i][0] for i in range(1, len(x))), reverse=True)
    print(lst)
    
    for music in lst:
        if len(music) == 2:
            answer.append(music[1][1])
        elif len(music) == 3:
            if music[1][0] > music[2][0]:
                answer.append(music[1][1])
                answer.append(music[2][1])
            else:
                answer.append(music[2][1])
                answer.append(music[1][1])
        else:
            box = [0,0]
            idx = [-1,-1]
            for k in range(1,len(music)):
                if music[k][0] > box[0]:
                    box[1] = box[0]
                    box[0] = music[k][0]
                    idx[1] = idx[0]
                    idx[0] = music[k][1]
                elif music[k][0] > box[1]:
                    box[1] = music[k][0]
                    idx[1] = music[k][1]
            answer.append(idx[0])
            answer.append(idx[1])
            
    return answer