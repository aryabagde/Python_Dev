# -------------------------------
# BASIC / PRIMITIVE DATA TYPES
# -------------------------------

# int
a = 10
print("int:", a, type(a))

# float
b = 3.14
print("float:", b, type(b))

# complex
c = 2 + 3j
print("complex:", c, type(c))

# bool
d = True
print("bool:", d, type(d))

# NoneType
e = None
print("NoneType:", e, type(e))


# -------------------------------
# SEQUENCE DATA TYPES
# -------------------------------

# string
s = "Hello Python"
print("\nstring:", s, type(s))

# list (mutable)
lst = [1, 2, 3, "Python", 3.14]
lst.append(100)
print("list:", lst, type(lst))

# tuple (immutable)
tup = (10, 20, 30)
print("tuple:", tup, type(tup))

# range
r = range(1, 5)
print("range:", list(r), type(r))


# -------------------------------
# SET DATA TYPES
# -------------------------------

# set (unique, unordered)
st = {1, 2, 3, 3, 4}
print("\nset:", st, type(st))

# frozenset (immutable set)
fst = frozenset([1, 2, 3, 3])
print("frozenset:", fst, type(fst))


# -------------------------------
# MAPPING DATA TYPE
# -------------------------------

# dict (key-value pairs)
dic = {
    "name": "Arya",
    "age": 22,
    "student": True
}
print("\ndict:", dic, type(dic))


# -------------------------------
# BINARY DATA TYPES
# -------------------------------

# bytes (immutable)
by = b"ABC"
print("\nbytes:", by, type(by))

# bytearray (mutable)
ba = bytearray([65, 66, 67])
ba[0] = 97
print("bytearray:", ba, type(ba))

# memoryview
mv = memoryview(ba)
print("memoryview:", mv, type(mv))


# -------------------------------
# TYPE CONVERSION (TYPE CASTING)
# -------------------------------

x = 5
y = float(x)
z = str(x)

print("\nType casting:")
print("int to float:", y)
print("int to string:", z)


# -------------------------------
# CHECKING DATA TYPE
# -------------------------------

print("\nType checking:")
print(isinstance(lst, list))
print(isinstance(dic, dict))
print(isinstance(st, set))


# -------------------------------
# USER DEFINED DATA TYPE (CLASS)
# -------------------------------

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("\nStudent name:", self.name)
        print("Roll no:", self.roll)

s1 = Student("Arya", 1)
s1.display()
