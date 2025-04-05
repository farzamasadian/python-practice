sum=input()
sum=sum.split('+')
sum2=[]
sum3=[]
sum4=''
for i in sum:
    sum2.append(int(i))
sum2.sort()
for i in sum2:
    sum3.append(str(i))
for i in sum3:
    sum4+=i+'+'
sum4=sum4[:len(sum4)-1]
print(sum4)
