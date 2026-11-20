# Experiment 3(a)(i): Display all prime numbers up to a given number n using loops

n = int(input("Enter n: "))
primes = []

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(f"Prime numbers up to {n}:")
print(*primes)
print("Count:", len(primes))
