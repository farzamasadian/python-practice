import datetime
import sys


today=str(datetime.date.today())
today=today.split('-')

class Person:
    def __init__(self, birth_date):
        self.birth_date=birth_date

    def get_age(self):
        if int(today[1])>=self.birth_date[1]:
            return int(today[0]) - self.birth_date[0]
        else:
            return int(today[0]) - self.birth_date[0] - 1

birth_date=input('Birth date: ')
birth_date=birth_date.split('/')
birth_date_int=[int(i) for i in birth_date]
birth_date=birth_date_int

if birth_date_int[1]>12 or birth_date_int[1]<1:
    print('WRONG')
    sys.exit()
if birth_date_int[2]>31 or birth_date_int[2]<1:
    print('WRONG')
    sys.exit()
farzam=Person(birth_date_int)

print(farzam.get_age())