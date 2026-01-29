# ===============================
# COMMENTS
# ===============================
# This is a single-line comment

"""
This is a
multi-line comment (docstring)
"""

# ===============================
# PRINT & INPUT
# ===============================
print("Hello, Python!")

name = "Arya"          # variable assignment
age = 22
print("Name:", name, "Age:", age)

# ===============================
# DATA TYPES
# ===============================
x = 10                 # int
y = 3.5                # float
z = 2 + 3j              # complex
flag = True            # bool
nothing = None         # NoneType

# ===============================
# TYPE CHECKING & CASTING
# ===============================
print(type(x))
print(isinstance(y, float))

a = "100"
b = int(a)             # type casting
print(b + 20)

# ===============================
# OPERATORS
# ===============================
# Arithmetic
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# Comparison
print(5 > 3)
print(5 == 3)
print(5 != 3)

# Logical
print(True and False)
print(True or False)
print(not True)

# ===============================
# STRINGS
# ===============================
s = "Python"
print(s[0])            # indexing
print(s[1:4])          # slicing
print(s.lower())
print(s.upper())
print(len(s))

# ===============================
# LIST
# ===============================
lst = [1, 2, 3]
lst.append(4)
lst.remove(2)
print(lst)

# ===============================
# TUPLE
# ===============================
tup = (10, 20, 30)
print(tup[1])

# ===============================
# SET
# ===============================
st = {1, 2, 3, 3}
st.add(4)
print(st)

# ===============================
# DICTIONARY
# ===============================
dic = {"name": "Arya", "age": 22}
dic["age"] = 23
print(dic)
print(dic["name"])

# ===============================
# IF - ELIF - ELSE
# ===============================
num = 10

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# ===============================
# LOOPS
# ===============================
# for loop
for i in range(1, 4):
    print("For loop:", i)

# while loop
count = 0
while count < 3:
    print("While loop:", count)
    count += 1

# break and continue
for i in range(5):
    if i == 3:
        break
    if i == 1:
        continue
    print("Loop control:", i)

# ===============================
# FUNCTIONS
# ===============================
def add(a, b):
    return a + b

result = add(5, 3)
print("Function result:", result)

# default argument
def greet(name="Guest"):
    print("Hello", name)

greet("Arya")
greet()

# ===============================
# LAMBDA FUNCTION
# ===============================
square = lambda x: x * x
print("Lambda:", square(5))

# ===============================
# EXCEPTION HANDLING
# ===============================
try:
    x = int("abc")
except ValueError:
    print("Conversion failed")
finally:
    print("Exception handled")

# ===============================
# CLASS & OBJECT
# ===============================
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

s1 = Student("Arya", 1)
s1.display()

# ===============================
# FILE HANDLING (BASIC)
# ===============================
file = open("demo.txt", "w")
file.write("Hello File")
file.close()

file = open("demo.txt", "r")
print(file.read())
file.close()

# ===============================
# IMPORT MODULE
# ===============================
import math
print(math.sqrt(16))
