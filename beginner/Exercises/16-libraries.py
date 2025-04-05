import math
n=int(input('Please enter the number of inputs'))
l=[]
for i in range(n):
    number=int(input('Please enter the number'))
    l.append(number)
m=[math.sqrt(i) for i in l]
# m=['{0:.4f}'.format(i) for i in m]  ***** it rounds the numbers after the selected decimal however
m=[math.trunc(i*10000)/10000 for i in m]
m=['{0:.4f}'.format(i) for i in m]
[print(i) for i in m]