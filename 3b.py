# Experiment 3(b): Read each line of a file and print its characters in reverse order
import os

filename = input("Enter file name (default: sample3b.txt): ").strip() or "sample3b.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Hello World\nPython Programming\nJSPM University\n")
    print(f"'{filename}' not found - created a sample file.")

with open(filename, "r") as f:
    for line_no, line in enumerate(f, start=1):
        line = line.rstrip("\n")
        reversed_line = ""
        for ch in line:                 # build reversed string using a loop
            reversed_line = ch + reversed_line
        print(f"Line {line_no}: {line}  ->  {reversed_line}")
