# Experiment 9: Library Management System
# Classes, inheritance, polymorphism and persistent storage (JSON)
import json
import os
from datetime import date, timedelta

DB_FILE = "library_data_9.json"


# ---------------- Item hierarchy (inheritance + polymorphism) ----------------
class LibraryItem:
    LOAN_DAYS = 14
    FINE_PER_DAY = 1

    def __init__(self, item_id, title, author, available=True, borrower=None, due_date=None):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.available = available
        self.borrower = borrower
        self.due_date = due_date

    def kind(self):
        return "Item"

    def calculate_fine(self, return_date=None):
        if not self.due_date:
            return 0
        return_date = return_date or date.today()
        late = (return_date - date.fromisoformat(self.due_date)).days
        return max(0, late) * self.FINE_PER_DAY

    def describe(self):
        status = "Available" if self.available else f"Issued to {self.borrower} (due {self.due_date})"
        return f"[{self.kind():<8}] {self.item_id:<5}{self.title:<28}{self.author:<18}{status}"

    def to_dict(self):
        d = self.__dict__.copy()
        d["type"] = self.__class__.__name__
        return d


class Book(LibraryItem):
    LOAN_DAYS = 14
    FINE_PER_DAY = 2

    def kind(self):
        return "Book"


class Magazine(LibraryItem):
    LOAN_DAYS = 7
    FINE_PER_DAY = 1

    def kind(self):
        return "Magazine"


class DVD(LibraryItem):
    LOAN_DAYS = 3
    FINE_PER_DAY = 5

    def kind(self):
        return "DVD"


TYPES = {"Book": Book, "Magazine": Magazine, "DVD": DVD}


# ---------------- Library ----------------
class Library:
    def __init__(self, db_file=DB_FILE):
        self.db_file = db_file
        self.items = {}
        self.load()

    def add_item(self, item):
        if item.item_id in self.items:
            raise ValueError("Item ID already exists")
        self.items[item.item_id] = item
        self.save()

    def issue(self, item_id, member):
        item = self._get(item_id)
        if not item.available:
            raise ValueError("Item is already issued")
        item.available = False
        item.borrower = member
        item.due_date = (date.today() + timedelta(days=item.LOAN_DAYS)).isoformat()
        self.save()
        return item.due_date

    def return_item(self, item_id, return_date=None):
        item = self._get(item_id)
        if item.available:
            raise ValueError("Item was not issued")
        fine = item.calculate_fine(return_date)
        item.available, item.borrower, item.due_date = True, None, None
        self.save()
        return fine

    def search(self, text):
        t = text.lower()
        return [i for i in self.items.values() if t in i.title.lower() or t in i.author.lower()]

    def _get(self, item_id):
        if item_id not in self.items:
            raise KeyError("Item not found")
        return self.items[item_id]

    def display_all(self):
        if not self.items:
            print("Library is empty.")
        for item in self.items.values():
            print(item.describe())          # polymorphic call

    def save(self):
        with open(self.db_file, "w") as f:
            json.dump([i.to_dict() for i in self.items.values()], f, indent=2)

    def load(self):
        if os.path.exists(self.db_file):
            with open(self.db_file) as f:
                for d in json.load(f):
                    cls = TYPES[d.pop("type")]
                    obj = cls(**d)
                    self.items[obj.item_id] = obj


def seed(lib):
    if not lib.items:
        lib.add_item(Book("B101", "Python Crash Course", "Eric Matthes"))
        lib.add_item(Book("B102", "Automate the Boring Stuff", "Al Sweigart"))
        lib.add_item(Magazine("M201", "Wired - Nov 2026", "Wired Staff"))
        lib.add_item(DVD("D301", "The Social Network", "David Fincher"))


def menu():
    lib = Library()
    seed(lib)
    while True:
        print("\n==== Library Management ====")
        print("1. Display all  2. Add item  3. Issue  4. Return  5. Search  6. Exit")
        ch = input("Choice: ").strip()
        try:
            if ch == "1":
                lib.display_all()
            elif ch == "2":
                t = input("Type (Book/Magazine/DVD): ").strip().title()
                if t == "Dvd":
                    t = "DVD"
                lib.add_item(TYPES[t](input("ID: "), input("Title: "), input("Author: ")))
                print("Added.")
            elif ch == "3":
                due = lib.issue(input("Item ID: "), input("Member name: "))
                print("Issued. Due date:", due)
            elif ch == "4":
                iid = input("Item ID: ")
                rd = input("Return date YYYY-MM-DD (blank = today): ").strip()
                fine = lib.return_item(iid, date.fromisoformat(rd) if rd else None)
                print("Returned. Fine: Rs.", fine)
            elif ch == "5":
                for i in lib.search(input("Search text: ")):
                    print(i.describe())
            elif ch == "6":
                print("Data saved. Goodbye!")
                break
            else:
                print("Invalid choice.")
        except (ValueError, KeyError) as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()
