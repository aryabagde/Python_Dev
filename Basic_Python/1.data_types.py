# ===============================
# PYTHON DATA TYPES - ALL IN ONE (WE don't have to mention the type of variables like C/C++)
# ===============================

# -------- 1. Numeric Types --------
integer_num = 10            # int
float_num = 3.14            # float
complex_num = 2 + 3j        # complex

print("Numeric Types:")
print(type(integer_num), integer_num)
print(type(float_num), float_num)
print(type(complex_num), complex_num)
print()

# -------- 2. Boolean --------
is_python_easy = True

print("Boolean:")
print(type(is_python_easy), is_python_easy)
print()

# -------- 3. String --------
string_data = "Hello, Python"

print("String:")
print(type(string_data), string_data)
print()

# -------- 4. List (Mutable, Ordered) --------
list_data = [1, 2, 3, "python", 4.5]

print("List:")
print(type(list_data), list_data)
print()

# -------- 5. Tuple (Immutable, Ordered) --------
tuple_data = (1, 2, 3, "python", 4.5)

print("Tuple:")
print(type(tuple_data), tuple_data)
print()

# -------- 6. Set (Mutable, Unordered, Unique) --------
set_data = {1, 2, 3, 3, 4}

print("Set:")
print(type(set_data), set_data)
print()

# -------- 7. Frozen Set (Immutable Set) --------
frozen_set_data = frozenset([1, 2, 3, 3, 4])

print("Frozen Set:")
print(type(frozen_set_data), frozen_set_data)
print()

# -------- 8. Dictionary (Key-Value Pairs) --------
dict_data = {
    "name": "Arya",
    "age": 22,
    "course": "Data Science"
}

print("Dictionary:")
print(type(dict_data), dict_data)
print()

# -------- 9. None Type --------
none_data = None

print("None Type:")
print(type(none_data), none_data)
print()

# -------- 10. Bytes --------
bytes_data = b"Python"

print("Bytes:")
print(type(bytes_data), bytes_data)
print()

# -------- 11. Bytearray (Mutable Bytes) --------
bytearray_data = bytearray([65, 66, 67])

print("Bytearray:")
print(type(bytearray_data), bytearray_data)
print()

# -------- 12. Range --------
range_data = range(1, 5)

print("Range:")
print(type(range_data), list(range_data))
print()

# -------- 13. Type Conversion (Casting) --------
num_str = "100"
converted_int = int(num_str)

print("Type Casting:")
print(type(num_str), "->", type(converted_int), converted_int)
print()

# -------- 14. Check Data Type --------
x = 5.5
print("Using isinstance():")
print(isinstance(x, float))
print(isinstance(x, int))
