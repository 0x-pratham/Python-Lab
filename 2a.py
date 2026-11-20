# Experiment 2(a): Arithmetic, relational, assignment, logical, bitwise,
#                  ternary, membership and identity operators

a, b = 17, 5

print("--- Arithmetic ---")
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)

print("\n--- Relational ---")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n--- Assignment ---")
x = 10
print("x = 10        ->", x)
x += 5;  print("x += 5        ->", x)
x -= 3;  print("x -= 3        ->", x)
x *= 2;  print("x *= 2        ->", x)
x //= 4; print("x //= 4       ->", x)
x **= 3; print("x **= 3       ->", x)
x %= 7;  print("x %= 7        ->", x)
x <<= 2; print("x <<= 2       ->", x)

print("\n--- Logical ---")
p, q = True, False
print("p and q:", p and q)
print("p or q :", p or q)
print("not p  :", not p)

print("\n--- Bitwise (a=17 -> 10001, b=5 -> 00101) ---")
print("a & b  =", a & b)
print("a | b  =", a | b)
print("a ^ b  =", a ^ b)
print("~a     =", ~a)
print("a << 2 =", a << 2)
print("a >> 2 =", a >> 2)

print("\n--- Ternary ---")
print("Larger of a and b:", a if a > b else b)
num = 8
print(num, "is", "even" if num % 2 == 0 else "odd")

print("\n--- Membership ---")
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits     :", "apple" in fruits)
print("'mango' not in fruits :", "mango" not in fruits)
print("'th' in 'Python'      :", "th" in "Python")

print("\n--- Identity ---")
l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l1
print("l1 is l3     :", l1 is l3)
print("l1 is l2     :", l1 is l2)
print("l1 == l2     :", l1 == l2)
print("l1 is not l2 :", l1 is not l2)
