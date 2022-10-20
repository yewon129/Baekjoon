S = str(input())
alphs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ans = [-1] * 26

for i in range(26):
    for j in range(len(S)):
        if alphs[i] == S[j] and ans[i] == -1:
            ans[i] = j

for k in range(26):
    print(ans[k], end=' ')