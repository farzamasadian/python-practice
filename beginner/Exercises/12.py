n=int(input())
laptops=[]
k=0
for i in range (n):
    laptop=input()
    laptop=laptop.split()
    laptop=[int(j) for j in laptop]
    laptops.append(laptop)
for i in range(0,len(laptops)):
    for j in range(0,len(laptops)):
        if i != j:
            if laptops[i][0]<laptops[j][0] and laptops[i][1]>laptops[j][1]:
                k+=1   
if k > 0:
    print('happy irsa')
else:
    print('poor irsa')