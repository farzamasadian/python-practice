n1=int(input())
n2=input()
n2=n2.split()
n=0
for i in n2:
    i=int(i)
    n2[n]=i
    n+=1
print(n2)
n2.sort()
print(n2)
n=0
for j in n2:
    if j<=2:
        n+=1
        print(j)
print(n2[:n])
n2=n2[:n]
print(len(n2)//3)
