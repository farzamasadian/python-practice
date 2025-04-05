n=0
c=0
mnumber=0
while n<20:
    number=int(input())
    n+=1
    b=0
    for i in range(1,number+1) :
        if number % i == 0:
            b+=1
    if b>c:            
        c=b    
        mnumber=number

print(mnumber,c)