word=input('Word:')
word=word.strip()
word=word.lower()
letters=list(word)
letters=list(filter(lambda x: x!='a' and x!='i' and x!='o' and x!='u' and x!='e',letters))
l=[]
for i in letters:
    l.append('.')
    l.append(i)
word=''
for i in l:
    word+=i
print(word)
