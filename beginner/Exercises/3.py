number=int(input())

b=0
for i in range(1,number) :
    if number % i == 0:
        b+=1

if b<=2:
    print('%s is a prime number.' %number )
else:
    print('%s is not a prime number.' %number )