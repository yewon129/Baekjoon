N = int(input())
arr = [0]*N
for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    arr[i] = [age, name]

arr.sort(key = lambda x:x[0])

for i in range(N):
    print(arr[i][0], arr[i][1])