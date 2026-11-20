# Experiment 3(a)(ii): Print the multiplication table of a given number using a loop

num = int(input("Enter a number: "))
limit = 10

print(f"\nMultiplication table of {num}")
for i in range(1, limit + 1):
    print(f"{num} x {i:2} = {num * i}")
