# Experiment 4(b): Pass/fail result from three subject marks using a class and object

class Student:
    PASS_MARK = 40          # minimum marks required in each subject

    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.marks = [m1, m2, m3]

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def result(self):
        return "PASS" if all(m >= self.PASS_MARK for m in self.marks) else "FAIL"

    def display(self):
        print("\n----- Result -----")
        print("Name       :", self.name)
        print("Marks      :", self.marks)
        print("Total      :", self.total())
        print(f"Percentage : {self.percentage():.2f}%")
        print("Result     :", self.result())


def read_mark(subject):
    while True:
        try:
            m = float(input(f"Enter marks in {subject} (0-100): "))
            if 0 <= m <= 100:
                return m
        except ValueError:
            pass
        print("Invalid marks, try again.")


name = input("Enter student name: ")
s = Student(name, read_mark("Subject 1"), read_mark("Subject 2"), read_mark("Subject 3"))
s.display()
