N,M = map(int,input().split())
l = []
for i in range(M):
    a,b = input().split()
    a = int(a)
    l.append([a,b])
for i in range(1,N+1):
    st = ""
    for j in range(M):
        if i % l[j][0] == 0:
            st = st + l[j][1] + " "
    if st == "":
        print(i)
    else:
        st = st.rstrip(" ")
        print(st)