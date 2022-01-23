a = list(map(int,input().split()))
for i in range(1,a[0]+1):
    if i % a[1] == 0 and i % a[2] != 0:
        print("A")
    elif i % a[1] != 0 and i % a[2] == 0:
        print("B")
    elif i % a[1] == 0 and i % a[2] == 0:
        print("AB")
    else:
        print("N")