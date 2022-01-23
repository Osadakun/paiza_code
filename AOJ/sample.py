N,D = map(int, input().split())
sum = D
for i in range(N-1):
    z = int(input())
    z = D - z
    sum += z

print(sum*D)