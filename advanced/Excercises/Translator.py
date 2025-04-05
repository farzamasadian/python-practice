from collections import OrderedDict
n=int(input('number of words: '))
full_list=[]
m=0
translated=''
od_eng=OrderedDict()
od_fr=OrderedDict()
od_ger=OrderedDict()
for i in range(n+1):
    word = input()
    word.strip()
    word=word.lower()
    m+=1
    each_word_list=[]
    if m<n+1:
        for each in word.split(' '):
            each_word_list.append(each)
        full_list.append(each_word_list)
    if m==n+1:
        sentence=word
        sentence.strip()
for i in full_list:
        od_eng[i[0]]=i[1]
        od_fr[i[0]]=i[2]
        od_ger[i[0]]=i[3]
dict_list=[]
value_list=[]
dict_list.append(od_eng)
dict_list.append(od_fr)
dict_list.append(od_ger)
value_list=list(od_eng.values())
value_list+=list(od_fr.values())
value_list+=list(od_ger.values())
sentence=sentence.split(' ')
for each in sentence:
    if each in value_list:
        for i in dict_list:
                for k in list(i.values()):
                    if each == k:
                        for j in i:
                            if i[j]==k:
                                translated+=j+' '
    else:
         translated+=each+' '
                            
print(translated)                     
                    