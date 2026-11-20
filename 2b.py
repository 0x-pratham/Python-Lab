# Experiment 2(b): Count the frequency of characters in a text file
import os

filename = input("Enter text file name (default: sample2b.txt): ").strip() or "sample2b.txt"

# Create a sample file if the file does not exist
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Python is a powerful programming language.\nIt is easy to learn!")
    print(f"'{filename}' not found - created a sample file.")

freq = {}
try:
    with open(filename, "r") as f:
        for ch in f.read():
            freq[ch] = freq.get(ch, 0) + 1
except FileNotFoundError:
    print("File not found.")
    raise SystemExit

print("\n{:<12}{}".format("Character", "Frequency"))
print("-" * 22)
for ch, count in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])):
    label = repr(ch) if ch.isspace() else ch
    print("{:<12}{}".format(label, count))
print("\nTotal characters:", sum(freq.values()))
