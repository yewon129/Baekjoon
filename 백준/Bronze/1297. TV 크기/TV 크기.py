D, H, W = map(int, input().split())

n = D / ((H**2 + W**2)**0.5)
print(int(H*n), int(W*n))