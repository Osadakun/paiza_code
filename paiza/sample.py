a,b = map(int,input().split())
a *= 100
flag = True
s = a+b
for i in range(10):
    for j in range(1,10):
        z = j * 10
        l = i + z
        l *= i
        ans = s
        ans += z
        if ans == l:
            print("%d %d" %(j,i))
            flag = False
            break
if flag:
    print("No")