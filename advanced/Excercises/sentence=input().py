sentence=input()
sentence_list=sentence.split('.')
sentence_list=[each.strip() for each in sentence_list]
sentence_list.remove('')
sentence_list=[each.split(' ') for each in sentence_list]
sentence_dict=dict()
n=0
lens=[]
for each in sentence_list:
    lens.append(len(each))
for each in sentence_list:
    n+=1
    for word in each:
        if each.index(word)!=0:
            if word[0].isupper()==True and n<=1:
                sentence_dict[str(each.index(word)+1)]=word
            if word[0].isupper()==True and n>1:
                sentence_dict[str(each.index(word)+1+(lens[n-2]))]=word

for i , j in sentence_dict.items():
    print(i,':',j)
