a,b = map(int, input().split())
n = int(input())
for i in range(n):
    c,d = map(int,input().split())
    if a > c:
        print("High")
    elif a == c:
        if b < d:
            print("High")
        else:
            print("Low")
    else:
        print("Low")