# Experiment 1(b): Accept a student's name, age and course and display the details

name = input("Enter student name   : ").strip()
while True:
    try:
        age = int(input("Enter student age    : "))
        if age <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive integer for age.")
course = input("Enter course         : ").strip()

print("\n===== Student Details =====")
print("Name   :", name)
print("Age    :", age)
print("Course :", course)
print("===========================")
