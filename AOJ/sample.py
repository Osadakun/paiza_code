N = int(input())
a,b = map(int, input().split())

l = [False]*(N +max(a,b))
l[0] = True
for i in range(N):
    if l[i]:
        l[i+a] = True
        l[i+b] = True
ans = l[:N].count(False)
print(ans)