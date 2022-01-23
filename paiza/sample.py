N = int(input())
l = []
for i in range(N):
    x = int(input())
    l.append(x)
M = int(input())
for i in range(M):
    a,b,c = map(int,input().split())
    if l[a-1] < c:
        l[b-1] += l[a-1]
        l[a-1] -= l[a-1]
    else:
        l[a-1] -= c
        l[b-1] += c
for i in range(N):
    print(l[i])