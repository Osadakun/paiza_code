n,m,t,k = map(int,input().split()) # 発言数，監視時間，対象期間，回数
cnt = 1+m-t
l = [[0 for j in range(m)] for i in range(n)]
for i in range(m):
    kom = list(map(int,input().split()))
    for j in range(n):
        l[j][i] = kom[j]
for i in range(n):
    for j in range(cnt):
        l_a = l[i]
        ans = sum(l_a[0:t])
        l[i].remove(l[i][0])
        if k - ans<= 0:
            print("yes %d" %(j+t))
            break
        else:
            if j == cnt-1:
                print("no 0")
