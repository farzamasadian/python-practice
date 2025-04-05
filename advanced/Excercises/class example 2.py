class Computer:
    count=0
    def __init__(self, ram, hard, cpu):
        Computer.count+=1
        self.ram=ram
        self.hard=hard
        self.cpu=cpu
    def value(self):
        return self.ram+self.hard+self.cpu
    def __del__(self):
        Computer.count-=1
class Laptop(Computer):
    count=0
    def value(self):
        count+=1
        return self.ram+self.hard+self.cpu+self.size 

pc1=Computer(12, 2, 4)
pc2=Computer(8, 4, 4)
laptop1=Laptop(16,2,4)
laptop1.size=13

print(pc1.value())
print(pc2.value())
print(laptop1.value())
print(Computer.count)
del pc1
print(Computer.count)