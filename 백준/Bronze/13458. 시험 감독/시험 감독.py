N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for i in range(N):
    answer += 1
    if lst[i] < B:
        pass
    else:
        lst[i] -= B
        if lst[i] % C > 0:
            answer += lst[i]//C + 1
        else:
            answer += lst[i]//C

print(answer)