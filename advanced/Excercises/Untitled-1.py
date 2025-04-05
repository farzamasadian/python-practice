dic=dict()
n=0
m=0
l=[]
for i in range(10):
    number=int(input('please enter your number'))
    n=0
    for j in range(2,number+1):
        if number%j == 0:
            m=0
            for k in range(1,j+1):  
                if j%k == 0:
                    m+=1
            if m<=2:
                n+=1
        dic[number]=n

for each in dic:
    if dic[each] == max(list(dic.values())):
        if int(each) == max(list(dic.keys())):
            print(each, dic[each])
         
