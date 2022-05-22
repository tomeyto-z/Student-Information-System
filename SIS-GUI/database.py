# THIS IS THE STUDENT RECORDS DATA BASE
import os
import csv

student_fields = ['STUDENT NO.', 'LAST NAME', 'FIRST NAME', 'MIDDLE NAME', 'EMAIL', 'CONTACT NO.']
student_database = 'students.csv'


def add(student_data):
    global student_database
    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])


def view(person):
    global student_fields
    global student_database

    os.system('cls')
    print("-" * 140)
    print("Enrolled Students".center(140))
    print("-" * 140)

    for x in student_fields:
        print(("|" + x + " ").ljust(20), end='')
    print("\n" + "-" * 140)

    if os.path.exists(student_database):
        if os.path.getsize(student_database) == 0:
            print("\nNo enrolled students")

        else:
            with open(student_database, "r", encoding="utf-8") as f:
                reader = csv.reader(f)

                for row in reader:
                    for item in row:
                        print(("|" + item + " ").ljust(20), end='')
                    print(" ")

        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            if person == "student":
                student.menu()
            else:
                faculty.menu()
        else:
            exit()
    else:
        print("\nNo enrolled students")
        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            if person == "student":
                student.menu()
            else:
                faculty.menu()
        else:
            exit()


def search(person):
    os.system('cls')
    print("-" * 40)
    print("Search Student".center(40))
    print("-" * 40)

    global student_fields
    global student_database

    roll = input("Enter student no. to search: ")

    if os.path.exists(student_database):
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        print("\nStudent Found\n")
                        for i in range(len(student_fields)):
                            print(student_fields[i].ljust(15) + ":" + row[i])
                        break
            else:
                print("\nStudent no. not found in our database")

        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            if person == "student":
                student.menu()
            else:
                faculty.menu()
        else:
            exit()
    else:
        print("\nStudent no. not found in our database")
        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            if person == "student":
                student.menu()
            else:
                faculty.menu()
        else:
            exit()


def update():
    os.system('cls')
    print("-" * 40)
    print("Update Student Information".center(40))
    print("-" * 40)

    global student_fields
    global student_database

    roll = input("Enter student no. to update: ")
    index_student = None
    updated_data = []

    if os.path.exists(student_database):
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        index_student = counter
                        print("Student Found: at index ", index_student)
                        print(" ")

                        student_data = []
                        for field in student_fields:
                            value = input("Enter " + field + ": ")
                            student_data.append(value)
                        updated_data.append(student_data)
                    else:
                        updated_data.append(row)
                    counter += 1

        # Check if the record is found or not
        if index_student is not None:
            with open(student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
        else:
            print("\nStudent no. not found in our database")

        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            student.menu()
        else:
            exit()

    else:
        print("\nStudent no. not found in our database")
        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            student.menu()
        else:
            exit()


def delete():
    global student_fields
    global student_database

    os.system('cls')
    print("-" * 40)
    print("Remove Student".center(40))
    print("-" * 40)

    roll = input("Enter student no. to delete: ")
    student_found = False
    updated_data = []

    if os.path.exists(student_database):
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if roll != row[0]:
                        updated_data.append(row)
                        counter += 1
                    else:
                        student_found = True

        if student_found is True:
            with open(student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("\nStudent no. ", roll, "deleted successfully")
        else:
            print("\nStudent no. not found in our database")

        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            student.menu()
        else:
            exit()

    else:
        print("\nStudent no. not found in our database")
        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            student.menu()
        else:
            exit()