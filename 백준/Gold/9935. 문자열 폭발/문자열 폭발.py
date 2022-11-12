import sys
input = sys.stdin.readline

s = input().rstrip()
# 비교를 쉽게 하기 위해 폭발 문자열을 리스트로 변형했다.
b = list(input().rstrip())
q = []

for i in s:
    q.append(i)
    if len(q) >= (len(b)):
        if q[-len(b):] == b:
            for _ in range(len(b)):
                q.pop()
print(*q if q else "FRULA",sep="")