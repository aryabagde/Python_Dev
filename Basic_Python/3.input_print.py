# =================================================
# INPUT() AND PRINT() — COMPLETE ONE-FILE GUIDE
# =================================================

# ---------------------------------
# 1. BASIC INPUT
# ---------------------------------

name = input("Enter your name: ")
print("Hello", name)
print()

# ---------------------------------
# 2. INPUT ALWAYS RETURNS STRING
# ---------------------------------

age = input("Enter your age: ")
print(type(age))     # str
print()

# ---------------------------------
# 3. TYPE CASTING INPUT
# ---------------------------------

age = int(input("Enter age (int): "))
height = float(input("Enter height (float): "))

print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
print()

# ---------------------------------
# 4. MULTIPLE INPUTS (SPACE SEPARATED)
# ---------------------------------

a, b = input("Enter two numbers: ").split()
a, b = int(a), int(b)

print("a =", a)
print("b =", b)
print()

# ---------------------------------
# 5. MULTIPLE INPUTS USING MAP
# ---------------------------------

x, y, z = map(int, input("Enter 3 integers: ").split())
print(x, y, z)
print()

# ---------------------------------
# 6. LIST INPUT
# ---------------------------------

numbers = list(map(int, input("Enter list of numbers: ").split()))
print(numbers)
print()

# ---------------------------------
# 7. PRINT BASIC USAGE
# ---------------------------------

print("Hello World")
print(10)
print(3.14)
print(True)
print()

# ---------------------------------
# 8. PRINT MULTIPLE VALUES
# ---------------------------------

a = 10
b = 20
print("a =", a, "b =", b)
print()

# ---------------------------------
# 9. SEP PARAMETER
# ---------------------------------

print("Python", "Java", "C++", sep=" | ")
print()

# ---------------------------------
# 10. END PARAMETER
# ---------------------------------

print("Hello", end=" ")
print("World")
print()

# ---------------------------------
# 11. PRINT WITHOUT NEWLINE
# ---------------------------------

for i in range(3):
    print(i, end=" ")
print("\n")

# ---------------------------------
# 12. STRING FORMATTING WITH PRINT
# ---------------------------------

name = "Arya"
age = 22

# Old style
print("Name: %s, Age: %d" % (name, age))

# format()
print("Name: {}, Age: {}".format(name, age))

# f-string (BEST)
print(f"Name: {name}, Age: {age}")
print()

# ---------------------------------
# 13. PRINT WITH ESCAPE CHARACTERS
# ---------------------------------

print("Line1\nLine2")
print("Tab\tSpace")
print("Quote: \"Python\"")
print()

# ---------------------------------
# 14. RAW STRING PRINT
# ---------------------------------

print(r"C:\Users\Arya\Desktop")
print()

# ---------------------------------
# 15. PRINT VARIABLES WITH TYPE
# ---------------------------------

x = 5.5
print("Value:", x)
print("Type:", type(x))
print()

# ---------------------------------
# 16. PRINT USING * UNPACKING
# ---------------------------------

lst = [1, 2, 3, 4]
print(*lst)
print()

# ---------------------------------
# 17. PRINT DICTIONARY
# ---------------------------------

data = {"name": "Arya", "course": "DS"}
print(data)
print(*data)         # keys
print(*data.values())
print()

# ---------------------------------
# 18. TAKING CHARACTER INPUT
# ---------------------------------

ch = input("Enter a character: ")[0]
print("Character:", ch)
print()

# ---------------------------------
# 19. INPUT ERROR HANDLING
# ---------------------------------

try:
    num = int(input("Enter integer: "))
    print("You entered:", num)
except ValueError:
    print("Invalid integer!")
print()

# ---------------------------------
# 20. INPUT UNTIL CONDITION
# ---------------------------------

while True:
    s = input("Enter 'q' to quit: ")
    if s == 'q':
        break
print("Exited loop")
print()

# ---------------------------------
# 21. FAST INPUT (IMPORTANT FOR CP)
# ---------------------------------

import sys

print("Using sys.stdin.readline():")
line = sys.stdin.readline().strip()
print(line)
print()

# ---------------------------------
# 22. PRINT TO FILE
# ---------------------------------

with open("output.txt", "w") as f:
    print("Hello File", file=f)

print("Written to file")
print()

# ---------------------------------
# 23. PRINT FLUSH (REAL-TIME OUTPUT)
# ---------------------------------

import time

for i in range(3):
    print(i, flush=True)
    time.sleep(1)

print("\n===== END OF INPUT & PRINT GUIDE =====")
