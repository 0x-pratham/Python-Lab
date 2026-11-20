# Experiment 4(a): Copy the contents of one text file into another file
import os

src = input("Enter source file (default: source4a.txt): ").strip() or "source4a.txt"
dst = input("Enter destination file (default: copy4a.txt): ").strip() or "copy4a.txt"

if not os.path.exists(src):
    with open(src, "w") as f:
        f.write("This is the source file.\nIt will be copied into another file.\n")
    print(f"'{src}' not found - created a sample file.")

try:
    with open(src, "r") as fin, open(dst, "w") as fout:
        for line in fin:
            fout.write(line)
    print(f"Contents of '{src}' copied to '{dst}' successfully.\n")
    print("--- Destination file contents ---")
    with open(dst) as f:
        print(f.read())
except OSError as e:
    print("Error:", e)
