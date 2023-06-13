N, M = map(int, input().split())
S = set(str(input()) for _ in range(N))
answer = 0

for i in range(M):
    word = str(input())
    if word in S:
        answer += 1

print(answer)