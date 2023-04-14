def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            w = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = w
    sizes.sort(reverse=True)
    w = sizes[0][0]
    sizes.sort(key=lambda x: x[1], reverse=True)
    h = sizes[0][1]
    return w*h