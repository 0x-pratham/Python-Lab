# Experiment 7: Demonstration of lambda functions
from functools import reduce

# 1. Basic lambda
square = lambda x: x * x
add = lambda a, b: a + b
print("square(6) =", square(6))
print("add(4, 9) =", add(4, 9))

# 2. Lambda with default argument and conditional expression
greet = lambda name, msg="Hello": f"{msg}, {name}!"
print(greet("Python"), "|", greet("JSPM", "Welcome"))
max_of = lambda a, b: a if a > b else b
print("max_of(12, 30) =", max_of(12, 30))

# 3. map(), filter(), reduce()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nnums             :", nums)
print("map (cubes)      :", list(map(lambda x: x ** 3, nums)))
print("filter (even)    :", list(filter(lambda x: x % 2 == 0, nums)))
print("reduce (product) :", reduce(lambda a, b: a * b, nums))
print("reduce (sum)     :", reduce(lambda a, b: a + b, nums))

# 4. Sorting with lambda as key
students = [("Aarav", 88), ("Diya", 95), ("Rohan", 67), ("Sneha", 74)]
print("\nSorted by marks (desc):", sorted(students, key=lambda s: s[1], reverse=True))
print("Sorted by name length :", sorted(students, key=lambda s: len(s[0])))
words = ["banana", "kiwi", "apple", "fig"]
print("Words sorted by length:", sorted(words, key=lambda w: len(w)))

# 5. Lambda inside a function (closure) - function factory
def multiplier(n):
    return lambda x: x * n

double, triple = multiplier(2), multiplier(3)
print("\ndouble(7) =", double(7), "| triple(7) =", triple(7))

# 6. Lambda in a dictionary (simple calculator)
ops = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
       "*": lambda a, b: a * b, "/": lambda a, b: a / b if b else "Division by zero"}
for sym, fn in ops.items():
    print(f"20 {sym} 4 = {fn(20, 4)}")
