import sys
arr = [str(input()) for _ in range(5)]
lines = [0] * 5

for i in range(5):
    lines[i] = len(arr[i])

answer = ''
for i in range(max(lines)):
    for j in range(len(arr)):
        if lines[j] > i:
            answer += arr[j][i]

print(answer)