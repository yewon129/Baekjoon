F, S, G, U, D = map(int, input().split())

v = [0] * (F+1)

def bfs(i):
    v[i] = 1
    q = [i]
    while q:
        i = q.pop(0)
        if i == G:
            return v[i]-1
        ui = i+U
        di = i-D
        if 0<ui<=F and v[ui] == 0:
            v[ui] = v[i] + 1
            q.append(ui)
        if 0<di<=F and v[di] == 0:
            v[di] = v[i] + 1
            q.append(di)

    return "use the stairs"


answer = bfs(S)
print(answer)