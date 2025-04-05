a=int(input())
b=0
c=0
while a != -1:
    a=int(input())
    if a == -1:
        break
    elif a > c:
        if a>b:
            c=b
            b=a 
        else:
            c=a
        
print(b,c)