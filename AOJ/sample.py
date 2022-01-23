l1 = []
l2 = []
max_ans = 0
n, le = map(int,input().split())
for i in range((n+1)*le):
    x = int(input())
    if i < le:
        l1.append(x)
    else:
        l2.append(x)
for i in range(n):
    max = 100
    for j in range(le):
        z = l1[j] - l2[j]
        if z == 0:
            max = max
        elif 0 < z < 11 or -11 < z < 0:
            max -= 1
        elif 10 < z < 21 or -21 < z < -10:
            max -= 2
        elif 20 < z < 31 or -31 < z < -20:
            max -= 3
        else:
            max -= 5
    if max_ans < max:
        max_ans = max
    for c in range(n):
        l2.remove(l2[c])
print((max_ans))