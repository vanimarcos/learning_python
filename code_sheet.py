# this is a inline comment in python 

"""
    This is a multiline coment in python  
"""

# varbles and numbers in python
numb_one = 2
numb_two = 3.5

# print resut of multiplication 
print(numb_one * numb_two)

# strings in python

hello_world = "Hello World"
print(hello_world)


# casting values 
cast_one = str(numb_one)
#print(cast_one)

cast_two = int(numb_two)
#print(cast_two)

cast_three = float(2)
#print all values in one 
print(cast_one, cast_two, cast_three)

"""
Python has the following data types bilt-in by default, in these categories:

Text Type: str
Numberic Types:     int, float, complex
Sequence Types:     list tuples, range
Mapping Type:       dict
Set Types:          set, frozenset
Bollean Type:       bool
Binary Type:        bytes, bytearray, memoryview

"""
# examples of those types

a = "Hello World Once Again" # string value 
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) 

# to get the length of a string we need to use
print(len(hello_world))
has_hello = "Hello" in hello_world
print(has_hello)
has_not_hello = "Hello" is not hello_world
print(has_not_hello)

b = 20.1 # integer 
c = 12j # a complex number
d = ["apple","banana","cherry"] # a list 
e = ("apple", "banana", "cherry") # a tuple 
f = range(6)
g = {"name": "Maya", "surname": "Marcel"} 
h = {"apple", "banana", "cherry"}
i = frozenset({"apple", "banana" ,"cherry"})
j = True
k = b"hello"
l = bytearray(5)
m = memoryview(bytes(5))


# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b 


# To cast a variable in pythoin we have 
# int(), float() and str()

# if statement
if b == 20 :
    print("The value of b is :", b)
else:
    print("The value of b is not 20") 

# single line if statement
print("Greater than 19") if b > 19 else print("Less or equals to 19")

# For loop in python
for x in "banana":
    print(x)

fruits = d
for x in fruits:
  print(x)
  if x == "banana":
    break

# While statement 
increment = 0 
while increment < 100 :
    increment += 1
    print(increment)


# Function in python
def my_function():
    print("Hello from my function")

my_function()

def helloWorld(username):
    print("Hello, " + username)

helloWorld("Vanilson")
helloWorld("Marcos")
helloWorld("Andrew")

#lambda Expressions

lamb = lambda x : x*2

print(lamb(2))

class my_class:
    x = 12 

cla = my_class()
print(cla.x)

# Arrays 
cars = ["Volvo", "Ford", "BMW"]
print(cars)

cars.append("Fiat")
print(cars)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printname(self):
        print(self.name, self.age)

p1 = Person("Vanilson Marcos", 12)

p1.printname()

# inheritance in python
class Student(Person):
    def __init__(self, name, age, grade, school_name):
        # calling the parent class constructor in the child class python
        super().__init__(name,age)
        self.grade = grade
        self.school_name = school_name


p2 = Student("Mario", 23, "12 G", "MPLA School")

p2.printname()


class Employee(Person):
    def __init__(self, name, age, company, position, salary):
        super().__init__(name, age)
        self.company = company
        self.position = position
        self.salary = salary


    def print_emp(self):
        print("Printing From class Employye")
        print("Name : ", self.name,  ", Salary: ", self.salary)

emp = Employee("Vanilson Marcos", 12, "Cetim Tech", "Software Developer", 420)
emp.print_emp()
emp.printname()

##inheritance one more time 

class Point():
    counter= 0

    def __init__(self, x, y):
        Point.counter += 1
        self.x = x
        self.y = y

    def draw_point(self):
        print("The point is in x: %d and in y: %d", self.x, self.y)

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def draw_point_3d(self):
        print("The point is position in x: %d and in y:%d and in z: %d", self.x, self.y, self.z)

point_one = Point(57, 65)
point_two = Point(9, 34)
point_three =  Point3D(3, 8, 44)

point_one.draw_point()

point_two.draw_point()

point_three.draw_point()
point_three.draw_point_3d()



print("Number of points created", Point.counter)








def calc_rec_area(a1, b1):
    return a1 * b1

res_area = calc_rec_area(b1=12, a1=98)

print("The res area is ", res_area) 


# adding module in python

import support
support.print_name("Hello World")

# input in python

#raw_input

# str_name = input("Enter your name here:")
# print(str_name)

# try:
#     fil = open("hello_world.txt", "w")
#     fil.write("This is hello world from a file using python")
# except IOError :
#     print("Error: can\'t find file or read data")
# else:
#     print("Written content in the file successfully")
#     fil.close()

    # more classes in python

