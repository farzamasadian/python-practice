from collections import OrderedDict

od=OrderedDict()
n = int(input('Please enter n'))
for i in range(n):
    word = input('Please enter the word')
    word=word.split(' ')
    od[word[0]] = word[1]
sentence = input('please enter the sentence')
sentence2=sentence
sentence2=sentence2.split(' ') 
sentence3=[]
for j in sentence2:
    j = od.get(j,j)
    sentence3.append(j)
sentence4=''
for i in range (len(sentence3)):
    sentence4 += ' ' + sentence3[i]
sentence4.strip()
print(sentence4)
