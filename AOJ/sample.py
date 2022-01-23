M = int(input())
l_M = []
flag = True
for i in range(M):
    x = int(input())
    l_M.append(x)
N = int(input())
l_N = []
for i in range(N):
    x = int(input())
    l_N.append(x)
for i in range(1,32):
    if i in l_M and i not in l_N:
        print("A")
    elif i not in l_M and i in l_N:
        print("B")
    elif i in l_M and i in l_N:
        if(flag):
            print("A")
            flag = False
        else:
            print("B")
            flag = True
    else:
        print("x")