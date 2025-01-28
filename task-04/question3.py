X=int(input())
N=int(input())
L1=[]
n=1
while n**N<=X: 
    L1.append(n**N)  
    n+=1  
L2=[0]*(X+1)  
L2[0]=1  
for j in L1: 
    for i in range(X, j-1,-1):
        L2[i]+=L2[i-j]
print(L2[X])

