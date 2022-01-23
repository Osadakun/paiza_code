i = int(input())
sum = 0
f = 1
for i in range(i):
    x = int(input())
    if x > f:
        sum += x-f
    else:
        sum += f-x
    f = x
print(sum)