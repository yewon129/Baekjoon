N = int(input())
lst = [0] * N
ans = 0
def nqueen(x):
    global ans
    if x == N:
        ans += 1
        return
    else:
        for i in range(N):
            lst[x] = i
            if promising(x):
                nqueen(x+1)

def promising(x):
    for i in range(x):
        if lst[x] == lst[i] or abs(lst[x]-lst[i]) == abs(x-i):
            return False
    return True

nqueen(0)
print(ans)