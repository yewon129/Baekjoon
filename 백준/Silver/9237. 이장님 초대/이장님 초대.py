import sys

N = int(sys.stdin.readline())

tree = list(map(int, sys.stdin.readline().split()))

tree.sort(reverse=True)

for i in range(len(tree)):
    tree[i] = tree[i] + i + 1

print(max(tree)+1)