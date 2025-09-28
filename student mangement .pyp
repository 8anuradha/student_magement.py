# Student Record Management System
# Language: Python

import os

filename = "students.txt"

# Function to add student
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    with open(filename, "a") as f:
        f.write(f"{roll},{name},{marks}\n")
    print("✅ Student record added successfully!\n")

# Function to view all students
def view_students():
    if not os.path.exists(filename):
        print("No records found.\n")
        return
    with open(filename, "r") as f:
        data = f.readlines()
        if not data:
            print("No records found.\n")
        else:
            print("\n--- Student Records ---")
            for line in data:
                roll, name, marks = line.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
            print()

# Function to search student
def search_student():
    roll = input("Enter Roll No to search: ")
    found = False
    with open(filename, "r") as f:
        for line in f:
            r, name, marks = line.strip().split(",")
            if r == roll:
                print(f"✅ Found: Roll: {r}, Name: {name}, Marks: {marks}\n")
                found = True
    if not found:
        print("❌ Student not found.\n")

# Function to delete student
def delete_student():
    roll = input("Enter Roll No to delete: ")
    lines = []
    found = False
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for line in lines:
            r, name, marks = line.strip().split(",")
            if r != roll:
                f.write(line)
            else:
                found = True
    if found:
        print("✅ Student deleted successfully!\n")
    else:
        print("❌ Student not found.\n")

# Main Menu
while True:
    print("=== Student Record Management ===")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting... Thank you!")
        break
    else:
        print("❌ Invalid choice. Try again.\n")
