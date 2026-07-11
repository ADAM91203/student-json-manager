import json
import os

file_path = os.path.join(os.path.dirname(__file__), "students.json")

with open(file_path, "r") as file:
    students = json.load(file)

while True:
    print("\nStudent JSON Manager")
    print("1. Show all students")
    print("2. Count all students")
    print("3. Exit")
    print("4. Average age")
    print("5. Oldest student")
    print("6. Youngest student")
    print("7. Add new student")

    choice = input("Choose an option: ")

    if choice == "1":
        for student in students:
            print(student["name"], "is", student["age"], "years old")

    elif choice == "2":
        count = 0

        for student in students:
            count = count + 1

        print("Total students:", count)

    elif choice == "3":
        print("Goodbye")
        break

    elif choice == "4":
        total = 0

        for student in students:
            total = total + student["age"]

        average = total / len(students)

        print("Average age:", average)

    elif choice == "5":
        oldest = students[0]

        for student in students:
            if student["age"] > oldest["age"]:
                oldest = student

        print(oldest["name"], "is the oldest student")

    elif choice == "6":
        youngest = students[0]

        for student in students:
            if student["age"] < youngest["age"]:
                youngest = student

        print(youngest["name"], "is the youngest student")

    elif choice == "7":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))

        new_student = {
            "name": name,
            "age": age
        }

        students.append(new_student)

        with open(file_path, "w") as file:
            json.dump(students, file, indent=4)

        print("Student saved successfully")

    else:
        print("Invalid option")