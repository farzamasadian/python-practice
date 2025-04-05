class Class:
    def __init__(self, count, age, height, weight):
        self.count=count
        self.age=age
        self.height=height
        self.weight=weight     
    def get_count(self):
        return self.count
    def get_age(self):
        a=0
        for i in self.age:
          a+=i  
        return a/self.count
    
    def get_height(self):
        a=0
        for i in self.height:
          a+=i  
        return a/self.count    
    def get_weight(self):
        a=0
        for i in self.weight:
          a+=i  
        return a/self.count

def list_maker(x):
    x.strip()
    x=x.split(' ')
    x=[int(i) for i in x]
    return x

dic=dict()
n=0
for k in range(2):
    n+=1
    if n ==1:
        count=int(input('count: '))
        age=input('age: ')
        age = list_maker(age)
        height=input('height: ')
        height=list_maker(height)
        weight=input('weight: ')
        weight=list_maker(weight)
        k=Class(count, age, height, weight)
    
        dic['A']='A'
        dic['A_age']=k.get_age()
        dic['A_height']=k.get_height()
        dic['A_weight']=k.get_weight()

    else:
        count=int(input('count: '))
        age=input('age: ')
        age = list_maker(age)
        height=input('height: ')
        height=list_maker(height)
        weight=input('weight: ')
        weight=list_maker(weight)
        k=Class(count, age, height, weight)
        dic['B']='B'
        dic['B_age']=k.get_age()
        dic['B_height']=k.get_height()
        dic['B_weight']=k.get_weight()

for i in list(dic.values()):
    if i != 'A' and i != 'B':
        print(i)

if dic['A_height']>dic['B_height']:
    print(dic['A'])
if dic['B_height']>dic['A_height']:
    print(dic['B'])
if dic['B_height']==dic['A_height']:
    if dic['A_weight']<dic['B_weight']:
        print(dic['A'])
    if dic['A_weight']>dic['B_weight']:
        print(dic['B'])