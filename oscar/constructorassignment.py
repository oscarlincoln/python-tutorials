# write a program that prints the name attribute of a person and a talk method
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")

# creating an instance of the class person
oscar = Person("oscar")
print(oscar.name)
oscar.talk()