S = input()
S = S.replace("-", "")
x = S.count("0")
sum = 0 + x * 12
S = S.replace("0", "")
for i in S:
    sum += int(i) + 2
print(sum*2)