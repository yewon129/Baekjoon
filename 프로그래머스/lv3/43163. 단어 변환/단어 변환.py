minV = 0

def solution(begin, target, words):
    global minV
    minV = 10000
    answer = 0
    if target not in words:
        return 0
    
    visited = [0] * len(words)
    def dfs(word, cnt):
        global minV
        if word == target:
            if cnt < minV:
                minV = cnt
            return
        for i in range(len(words)):
            if visited[i] == 0:
                c = len(begin)
                for j in range(len(begin)):
                    if words[i][j] == word[j]:
                        c -= 1
                if c == 1:
                    visited[i] = 1
                    dfs(words[i], cnt + 1)
                    visited[i] = 0
    dfs(begin, 0)
    return minV