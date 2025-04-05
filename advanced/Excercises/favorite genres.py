from collections import OrderedDict

genre_od=OrderedDict()
genre_dict=dict()
n=int(input())
for i in range(n):
    genre=input()
    genre=genre.strip()
    genre_list=genre.split(' ')
    genre_list=[each.lower() for each in genre_list]
    genre_list=[each.capitalize() for each in genre_list]
    genre_od[genre_list[0]]=genre_list[1:len(genre_list)]
genre_od_list=list(genre_od.values())
genre_dict_list=[]
for each in genre_od_list:
    for i in each:
        genre_dict[i]=genre_dict.get(i,0)+1
for i,j in genre_dict.items():
    genre_dict_list.append((i,j))    
sorted_list=sorted(genre_dict_list, key=lambda x: (-x[1],x[0]))
for i,j in sorted_list:
    print(i,':',j)
        