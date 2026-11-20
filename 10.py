# Experiment 10: Student Record Management System
# OOP, exception handling, file handling and SQLite
import csv
import sqlite3

DB_NAME = "students_10.db"


# ---------------- Custom exceptions ----------------
class StudentError(Exception):
    """Base class for application errors."""


class DuplicateStudentError(StudentError):
    pass


class StudentNotFoundError(StudentError):
    pass


class InvalidDataError(StudentError):
    pass


# ---------------- Model ----------------
class Student:
    def __init__(self, roll_no, name, course, marks):
        if not str(roll_no).isdigit():
            raise InvalidDataError("Roll number must be numeric")
        if not name.strip():
            raise InvalidDataError("Name cannot be empty")
        try:
            marks = float(marks)
        except (TypeError, ValueError):
            raise InvalidDataError("Marks must be a number")
        if not 0 <= marks <= 100:
            raise InvalidDataError("Marks must be between 0 and 100")
        self.roll_no = int(roll_no)
        self.name = name.strip()
        self.course = course.strip()
        self.marks = marks

    def __str__(self):
        return f"{self.roll_no:<6}{self.name:<18}{self.course:<12}{self.marks:>6.1f}"


# ---------------- Database layer ----------------
class StudentDB:
    def __init__(self, db_name=DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("""CREATE TABLE IF NOT EXISTS students(
                                roll_no INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                course TEXT,
                                marks REAL)""")
        self.conn.commit()

    def add(self, s):
        try:
            self.conn.execute("INSERT INTO students VALUES (?,?,?,?)",
                              (s.roll_no, s.name, s.course, s.marks))
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise DuplicateStudentError(f"Roll number {s.roll_no} already exists")

    def get(self, roll_no):
        row = self.conn.execute("SELECT * FROM students WHERE roll_no=?", (roll_no,)).fetchone()
        if not row:
            raise StudentNotFoundError(f"No student with roll number {roll_no}")
        return Student(*row)

    def all(self):
        return [Student(*r) for r in self.conn.execute("SELECT * FROM students ORDER BY roll_no")]

    def update(self, roll_no, name=None, course=None, marks=None):
        s = self.get(roll_no)
        new = Student(roll_no, name or s.name, course or s.course, marks if marks not in (None, "") else s.marks)
        self.conn.execute("UPDATE students SET name=?, course=?, marks=? WHERE roll_no=?",
                          (new.name, new.course, new.marks, new.roll_no))
        self.conn.commit()

    def delete(self, roll_no):
        self.get(roll_no)
        self.conn.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
        self.conn.commit()

    def export_csv(self, filename="students_export_10.csv"):
        with open(filename, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["roll_no", "name", "course", "marks"])
            for s in self.all():
                w.writerow([s.roll_no, s.name, s.course, s.marks])
        return filename

    def import_csv(self, filename):
        added, skipped = 0, 0
        with open(filename, newline="") as f:           # raises FileNotFoundError if missing
            for row in csv.DictReader(f):
                try:
                    self.add(Student(row["roll_no"], row["name"], row["course"], row["marks"]))
                    added += 1
                except StudentError:
                    skipped += 1
        return added, skipped

    def stats(self):
        return self.conn.execute("SELECT COUNT(*), AVG(marks), MAX(marks), MIN(marks) FROM students").fetchone()


def print_table(students):
    print(f"{'Roll':<6}{'Name':<18}{'Course':<12}{'Marks':>6}")
    print("-" * 42)
    for s in students:
        print(s)
    if not students:
        print("(no records)")


def menu():
    db = StudentDB()
    while True:
        print("\n===== Student Record Management =====")
        print("1.Add 2.View all 3.Search 4.Update 5.Delete 6.Statistics 7.Export CSV 8.Import CSV 9.Exit")
        ch = input("Choice: ").strip()
        try:
            if ch == "1":
                db.add(Student(input("Roll no: "), input("Name: "), input("Course: "), input("Marks: ")))
                print("Student added.")
            elif ch == "2":
                print_table(db.all())
            elif ch == "3":
                print_table([db.get(int(input("Roll no: ")))])
            elif ch == "4":
                r = int(input("Roll no to update: "))
                print("Leave blank to keep the current value.")
                db.update(r, input("New name: "), input("New course: "), input("New marks: "))
                print("Updated.")
            elif ch == "5":
                db.delete(int(input("Roll no to delete: ")))
                print("Deleted.")
            elif ch == "6":
                n, avg, hi, lo = db.stats()
                print(f"Students: {n} | Average: {avg or 0:.2f} | Highest: {hi} | Lowest: {lo}")
            elif ch == "7":
                print("Exported to", db.export_csv())
            elif ch == "8":
                a, s = db.import_csv(input("CSV file name: "))
                print(f"Imported {a} record(s), skipped {s}.")
            elif ch == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Error: please enter a valid number.")
        except FileNotFoundError:
            print("Error: file not found.")
        except StudentError as e:
            print("Error:", e)
        except sqlite3.Error as e:
            print("Database error:", e)


if __name__ == "__main__":
    menu()
