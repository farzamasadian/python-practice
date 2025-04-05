n1=int(input())
n2=input()
n2=n2.split()
n3=[]
n2=[int(i) for i in n2]
[n3.append(j) for j in n2 if j<=2]    
print(n3)
print(len(n3)//3)