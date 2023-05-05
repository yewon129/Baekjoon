def solution(s):
    answer = []
    lst = s.split('},')
    my_lst = []
    for i in lst:
        i = i.replace('}','')
        i = i.replace('{','')
        box = i.split(',')
        my_lst.append(box)
        
    my_lst.sort(key=lambda x: len(x))
    
    for i in my_lst:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))
            
    return answer