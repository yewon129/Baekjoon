T = int(input())
for _ in range(T):
    lst = list(map(str, input()))
    box = []
    ans = 'YES'
    for i in range(len(lst)):
        if lst[i] == '(':
            box.append('(')
        else:
            if len(box) > 0:
                box.pop(0)
            else:
                ans = 'NO'
                break
    if len(box) != 0:
        ans = 'NO'

    print(ans)