class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        print(f'name is {self.name}')
    def get_age(self):
        print(f'{self.name}\'s age is {self.age}')
    def get_info(self):
        print(f'name is {self.name} and age is {self.age}')

farzam = Person('farzam',22)
jadi=Person('jadi',40)
farzam.get_info()