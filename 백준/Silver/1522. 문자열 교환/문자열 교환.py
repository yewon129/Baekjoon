st = input()
a_cnt = st.count('a')
m = len(st)
st = st + st[0:a_cnt-1]
for i in range(len(st)-a_cnt+1):
    box = st[i:i+a_cnt]
    m = min(m, box.count('b'))

print(m)