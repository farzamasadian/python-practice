a=int(input('Enter the number'))
c=str(a)
b=0
n=1
while n<=len(c):
    b=b*10+a%10
    a=a//10
    n+=1
print(b)

# b1=a%10
# a=a//10
# b2=a%10
# a=a//10
# b=b1*100+b2*10+a



# print(2*b)