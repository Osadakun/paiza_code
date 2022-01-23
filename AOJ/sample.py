l = input().split("+")
sum = 0
for i in range(len(l)):
    j = l[i].count("<")
    k = l[i].count("/")
    sum += j*10 + k
print(sum)