S=input()
L=[0,0,0,0,0,0,0,0,0,0]
for i in S:
    if i.isdigit():
        x=int(i)
        L[x]+=1
for j in L:
    print(j,"",end="")
