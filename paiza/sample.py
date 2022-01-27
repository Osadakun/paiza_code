h,w = map(int, input().split())
l = [[0]*w for i in range(h)]
ans = []
for i in range(h):
    s = list(map(int, input().split()))
    for j in range(w):
        l[i][j] = s[j]
for i in range(h):
    for j in range(1,w+1):
        a = sum(l[i][:j])
        b = sum(l[i][j:])
        if a == b:
            ans.append(j)
            break
if ans == []:
    print("No")
else:
    print("Yes")
    for i in range(h):
        a = ans[i]
        print("A"*a+"B"*(w-a))