# Let's チャレンジ！！
n,m = map(int,input().split())
l = []
ans = []
for i in range(n):
    a = list((map(int, input().split())))
    l.append(a)

for i in range(n):
    for j in range(n):
        x = l[j][i] - m
        if x < 0:
            if j == 2:
                ans.append(i+1)
        else:
            break
if len(ans) == 0:
    print("wait")
else:
    print(*ans)