n=int(input())
k=list(map(int,input().split()))
s1=sum(set(k))*n
s2=sum(k)
r=(s1-s2)/(n-1)
print(int(r))

