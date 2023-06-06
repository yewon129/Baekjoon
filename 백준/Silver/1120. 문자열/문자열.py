X, Y = map(str, input().split())
if len(X) == len(Y):
    answer = 0
    for i in range(len(Y)):
        if X[i] != Y[i]:
            answer += 1
    print(answer)
else:
    minV = len(Y)
    for i in range(len(Y)-len(X)+1):
        cnt = 0
        for j in range(len(X)):
            if X[j] != Y[i+j]:
                cnt += 1
        if cnt < minV:
            minV = cnt

    print(minV)