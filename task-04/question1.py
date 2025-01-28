n=int(input())
a=list(map(int,input().split()))
m = int(input())
b=list(map(int,input().split()))
l=[]
for i in b:
    if i in a:
        a.remove(i)
    else:
        l.append(i)
l.sort()
for i in l:
    print(i,"",end="")
