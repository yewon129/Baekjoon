N = int(input())
tree = {}

for _ in range(N):
    a,b,c = map(str, input().split())
    tree[a] = [b,c]

def first(root):
    if root != '.':
        print(root, end='')
        first(tree[root][0])
        first(tree[root][1])

def second(root):
    if root != '.':
        second(tree[root][0])
        print(root, end='')
        second(tree[root][1])

def third(root):
    if root != '.':
        third(tree[root][0])
        third(tree[root][1])
        print(root, end='')

first('A')
print()
second('A')
print()
third('A')