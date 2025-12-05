
"""
Docstring for functions.simple_functions.math_functions

create functions dealing with math problems. 
    simple
        add
        subtract
        multiply
        divide
    moderate
        power of
        squareroot
        etc.
    advanced
        phy
        calc
        etc.

"""

"""
# function to ask for an input as a number from user
def get_num():
    print("Enter a number")
    return input()
"""

# update get_num to check for int float or complex numbers. 
# if no number is found keep asking.
def get_num():
    num_entered = False
    x = 0
    while(not num_entered):
        x = input("Enter a number: ")
        try:
            x = int(x)
            num_entered = True
        except:
            try:
                x = float(x)
                num_entered = True
            except:
                try:
                    x = complex(x)
                    num_entered = True
                except:
                    print("Input is not a number. Try again.")

    return x


# call get_num
print(get_num())

# sum of 2 numbers
def add_two(a, b):
    return a+b

# call add_two
x = 5
y = 10
print(f"{x} + {y} = {add_two(x, y)}")

# sum of 3 numbers
def add_three(a, b, c):
    return a+b+c

# cal add_three
z = 15
print(f"{x} + {y} + {z} = {add_three(x, y, z)}")

# sub 2 num
def sub_two(a, b):
    return a-b

#call sub_two
print(f"{x} - {y} = {sub_two(x, y)}")
print(f"{y} - {x} = {sub_two(y, x)}")

# multiply 2 numbers
def multi(a, b):
    return a*b

# call multi
print(f"{x} x {y} = {multi(x, y)}")

"""
# divide 2 numbers
def divi(a, b):
    return a/b
"""

# new divide 2 numbers check for /0
def divi(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot Divide By Zero!"

# call divi
# will return float unless casted to int
print(f"{z} / {x} = {divi(z, x)}")
print(f"{z} / {x} = {int(divi(z, x))}")
print(f"{x} / {0} = {divi(x, 0)}") # cannot div by 0
