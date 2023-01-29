class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print("hello %s, are you %i years old?" % (self.name, self.age))

per1 = Person("maria", 28)
per1.get_info()