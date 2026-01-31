# ==========================================
# PYTHON STRINGS – COMPLETE ONE-FILE GUIDE
# ==========================================

print("===== STRING CREATION =====")

s1 = "Hello"
s2 = 'World'
s3 = """This is
a multiline
string"""
s4 = '''Another
multiline string'''

print(s1, s2)
print(s3)
print()

# ==========================================
# STRING TYPE & IMMUTABILITY
# ==========================================

print("===== STRING TYPE & IMMUTABILITY =====")

s = "Python"
print(type(s))

# s[0] = 'J'  # ❌ ERROR (strings are immutable)
print("Strings are immutable")
print()

# ==========================================
# STRING INDEXING & SLICING
# ==========================================

print("===== INDEXING & SLICING =====")

s = "PYTHON STRING"

print(s[0])       # P
print(s[-1])      # G
print(s[0:6])     # PYTHON
print(s[:6])      # PYTHON
print(s[7:])      # STRING
print(s[::-1])    # Reverse
print()

# ==========================================
# STRING CONCATENATION & REPETITION
# ==========================================

print("===== CONCATENATION & REPETITION =====")

a = "Hello"
b = "World"

print(a + " " + b)
print(a * 3)
print()

# ==========================================
# STRING ITERATION
# ==========================================

print("===== STRING ITERATION =====")

for ch in "ABC":
    print(ch, end=" ")
print("\n")

# ==========================================
# STRING LENGTH & MEMBERSHIP
# ==========================================

print("===== LENGTH & MEMBERSHIP =====")

s = "machine learning"

print(len(s))
print("machine" in s)
print("AI" not in s)
print()

# ==========================================
# STRING METHODS (MOST IMPORTANT)
# ==========================================

print("===== STRING METHODS =====")

s = "  Python Programming  "

print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace("Python", "C"))
print(s.find("Program"))
print(s.count("m"))
print(s.startswith("  Py"))
print(s.endswith("ing  "))
print()

# ==========================================
# SPLIT & JOIN (VERY IMPORTANT)
# ==========================================

print("===== SPLIT & JOIN =====")

sentence = "machine learning with python"

words = sentence.split()
print(words)

joined = "-".join(words)
print(joined)
print()

# ==========================================
# STRING FORMATTING (OLD → MODERN)
# ==========================================

print("===== STRING FORMATTING =====")

name = "Arya"
age = 22

# Old style
print("Name: %s, Age: %d" % (name, age))

# format()
print("Name: {}, Age: {}".format(name, age))

# f-string (BEST)
print(f"Name: {name}, Age: {age}")
print()

# ==========================================
# ESCAPE CHARACTERS & RAW STRINGS
# ==========================================

print("===== ESCAPE & RAW STRINGS =====")

print("Line1\nLine2")
print("Tab\tSpace")

raw_path = r"C:\Users\Arya\Desktop"
print(raw_path)
print()

# ==========================================
# STRING CHECKING METHODS
# ==========================================

print("===== STRING CHECKING =====")

s1 = "Python123"
s2 = "12345"

print(s1.isalpha())
print(s1.isalnum())
print(s2.isdigit())
print("   ".isspace())
print()

# ==========================================
# STRING COMPARISON
# ==========================================

print("===== STRING COMPARISON =====")

print("apple" == "apple")
print("apple" < "banana")  # lexicographical
print()

# ==========================================
# STRING ENCODING & DECODING (ML / NLP)
# ==========================================

print("===== ENCODING & DECODING =====")

text = "hello"

encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")

print(encoded)
print(decoded)
print()

# ==========================================
# STRING TO LIST & LIST TO STRING
# ==========================================

print("===== STRING ↔ LIST =====")

s = "ABCDE"

lst = list(s)
print(lst)

new_s = "".join(lst)
print(new_s)
print()

# ==========================================
# STRING MEMORY BEHAVIOR (IMPORTANT)
# ==========================================

print("===== MEMORY BEHAVIOR =====")

a = "python"
b = "python"

print(id(a))
print(id(b))   # same due to string interning
print()

# ==========================================
# COMMON STRING INTERVIEW TRICKS
# ==========================================

print("===== INTERVIEW TRICKS =====")

# Reverse string
s = "hello"
print(s[::-1])

# Palindrome
s = "madam"
print(s == s[::-1])

# Character frequency
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Remove duplicates
s = "aabbcc"
print("".join(set(s)))

print("\n===== END OF STRING GUIDE =====")
