
"""
Docstring for class_practice.simple_class

simple class with functions __init__ and tostr

"""

# Class is just a simple class with functions a to str and constructor.
# No rhyme or reason to this class. Just testing out class function calls
# and initalizing objects of class.
class Simple:
    def __init__(self, name = "Bob", age = 25):
        self.name = name
        self.age = age

    def addition(self, x, y):
        return x+y

    def __str__(self):
        return f"Object name is {self.name}. Age is {self.age}"


# init and use multiple objects of class Simple
simple = Simple()

print(simple.addition(5,19))
print(simple)

newSimple = Simple("Sue")

print(newSimple)


newNewSimple = Simple("Joe", 35)

print(newNewSimple.addition(5,5))
print(newNewSimple)
