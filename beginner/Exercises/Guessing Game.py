import random
upper=100
lower=1
a=input('enter')
b=random.randint(lower,upper)
print(b)
while a!='c':
    a=input('enter')
    if a=='s':
        upper=b-1
        b=random.randint(lower,upper)

    elif a=='b':
        lower=b+1
        b=random.randint(lower,upper)
    print(b)
