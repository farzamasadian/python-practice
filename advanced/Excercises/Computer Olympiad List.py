n = int(input('number of contestants: '))
l2=[]
for i in range(n):
    l1=[]
    name=input('names: ')
    name_list=name.split('.')
    for each in name_list:
        if name_list.index(each)==1:
            each=each.lower().capitalize()
            l1.append(each)
        else:
            l1.append(each)

    l2.append((l1[0],l1[1],l1[2]))
sorted_list=sorted(l2, key=lambda x:(x[0],x[1]))
for i,j,k in sorted_list:
    print(i,j,k)

