# Experiment 1(a): Fundamental Python data types (int, float, complex, bool, string)

a = 25                      # int
b = 3.14159                 # float
c = 4 + 7j                  # complex
d = True                    # bool
e = "Python Programming"    # str

values = [("int", a), ("float", b), ("complex", c), ("bool", d), ("string", e)]

print("{:<10}{:<25}{}".format("Name", "Value", "Type"))
print("-" * 50)
for name, val in values:
    print("{:<10}{:<25}{}".format(name, str(val), type(val)))

print("\n--- Operations on each type ---")
print("int     : a * 2 =", a * 2, "| a // 4 =", a // 4, "| a % 4 =", a % 4)
print("float   : round(b, 2) =", round(b, 2))
print("complex : real =", c.real, "| imag =", c.imag, "| conjugate =", c.conjugate(), "| abs =", abs(c))
print("bool    : True + True =", True + True, "| not d =", not d)
print("string  : upper =", e.upper(), "| length =", len(e), "| first word =", e.split()[0])

print("\n--- Type conversion ---")
print("int('42') =", int("42"))
print("float(7) =", float(7))
print("str(99) =", str(99), type(str(99)))
print("bool(0) =", bool(0), "| bool('hi') =", bool("hi"))
print("complex(2, 3) =", complex(2, 3))
