def cluc1(C,X):
    if X == "R":
        return C + 1
    else:
        return C - 1

def cluc2(C1,C2,X):
    if X == "R":
        return C1 + 1, C2 + 1
    else:
        return C1 - 1, C2 - 1

def cluc3(C1,C2,C3,X):
    if X == "R":
        return C1 + 1,C2 + 1,C3 + 1,
    else:
        return C1 - 1,C2 - 1,C3 - 1,

n = int(input())
R,G,B = map(int,input().split())
ans = "no"
for i in range(n):
    X, col = input().split()
    if col == "R":
        R = cluc1(R,X)
    elif col == "G":
        G = cluc1(G,X)
    elif col == "B":
        B = cluc1(B,X)
    elif col == "Y":
        R,G = cluc2(R,G,X)
    elif col == "M":
        R,B = cluc2(R,B,X)
    elif col == "C":
        B, G = cluc2(B,G,X)
    else:
        R,G,B = cluc3(R,G,B,X)
    if R == G == B:
        ans = R
        break

print(ans)