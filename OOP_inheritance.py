# parent object
class Computer:
    count = 0
    # constructor function
    def __init__(self, ram, cpu, hard):
        Computer.count += 1
        self.ram = ram
        self.cpu = cpu
        self.hard = hard

    def value(self):
        return self.ram+self.hard+self.cpu
    
    # detroier function
    def __del__(self):
        Computer.count -= 1

# child object who inherited from its parent
class Laptop(Computer):
    # pass
    def value(self, size):
        return self.ram+self.hard+self.cpu+size

com1 = Computer(20,7,2)
print(com1.value())
com2 = Computer(32,11,1)
print(com2.value())
del com2

lab1 = Laptop(12,8,2)
print(lab1.value(15))