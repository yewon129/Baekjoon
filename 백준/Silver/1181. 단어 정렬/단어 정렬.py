N = int(input())
arr = [str(input()) for _ in range(N)]

arr = list(set(arr))
arr.sort(key=lambda x: (len(x),x))

for word in arr:
    print(word)