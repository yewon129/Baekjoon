N , M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

v= [0] * N
stack = []

def dfs():
    if len(stack) == M:
        for i in range(M):
            print(stack[i], end=' ')
        print()
    else:
        for i in range(N):
            if v[i] == 0:
                stack.append(lst[i])
                v[i] = 1
                dfs()
                stack.pop()
                v[i] = 0

dfs()