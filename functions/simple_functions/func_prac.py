
"""
Docstring for functions.simple_functions.func_prac

Create multiple functions.
    some with no return
    some with return
    some with no arguments
    some with arguments
"""


# simple print statment. to say hello when function is called.
def hello():
    print("Hello!")

#call hello() function
hello()

# modify hello function to print hello + name where name is passed in as an argument.
def hello_name(name):
    print("Hello, " + name + "!")

# call hello_name()
hello_name("Bob")

# modify hello + name function print statment to use f and {} and not +
def hello_name_Mod(name):
    print("Hello, {name}!") #output is Hello, {name}!
    print(f"Hello, {name}!") #output is Hello, (name passed int)!

# call hello_name_Mod
hello_name_Mod("Sue")

# modify hello to ask user for name
def hello_user():
    print("What is your name?")
    name = input()
    print(f"Hello, {name}!")

# call hello_user
hello_user()

# create a function for asking for name that passed that name to another function for printing
def get_user_name():
    print("What is your name?")
    return input()

def hello_get_user():
    name = get_user_name()
    print(f"Hello, {name}!")

#call get user and print result then call hello_get_user
print(get_user_name())
hello_get_user()

