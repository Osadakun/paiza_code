m,q,p = map(float, input().split())
m -= (q*0.01) * m
m -= (p*0.01) * m
print(m)