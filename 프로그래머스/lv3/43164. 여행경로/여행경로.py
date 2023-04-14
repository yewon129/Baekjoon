import copy

def solution(tickets):
    answer = []
    visited = [0] * len(tickets)
    box = []
    def dfs(i, lst):
        if len(lst) == len(tickets)+1:
            box.append(0)
            box[-1] = copy.deepcopy(lst)
            return
        for j in range(len(tickets)):
            if lst[-1] == tickets[j][0] and visited[j] == 0:
                lst.append(tickets[j][1])
                visited[j] = 1
                dfs(j, lst)
                visited[j] = 0
                lst.pop()
    
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            visited[i] = 1
            dfs(i, [tickets[i][0], tickets[i][1]])
            visited[i] = 0

    if len(box) == 1:
        return box[0]
    else:
        box.sort()
        return box[0]
