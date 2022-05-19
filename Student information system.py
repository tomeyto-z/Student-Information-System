#This is the console application
import csv
import hashlib
import os

# Define global variables
student_fields = ['STUDENT NO.', 'LAST NAME', 'FIRST NAME', 'MIDDLE NAME', 'AGE', 'EMAIL', 'CONTACT NO.']
student_database = 'students.csv'


# Begin function  ---------------------------------------------------------------------------------------
def begin():
    os.system('cls')
    print("-" * 40)
    print("Information System".center(40))
    print("-" * 40)
    print("[Choice 1]: Faculty member")
    print("[Choice 2]: Student")
    print("[Choice 3]: Quit")

    choice = input("\nEnter the number of choice: ")

    if choice == "1":
        faculty_member()
    elif choice == "2":
        student()
    elif choice == "3":
        print("-" * 40)
        print("Thank you for using our system".center(40))
        print("-" * 40)
        input("\n\nPress enter to exit . . .")
        exit()
    else:
        begin()


def student():
    os.system('cls')
    print("-" * 40)
    print("Student module".center(40))
    print("-" * 40)
    print("\n[Choice 1]: Log in")
    print("[Choice 2]: Create an account")

    choice = input("\nEnter the number of choice: ")

    person = 'student'

    filename = "Student_Credentials.txt"
    if choice == "1":
        login(filename, person)

    elif choice == "2":
        signup(filename, person)

    else:
        student()


# for student data base -------------------------------------------------------------------------------
def student_menu():
    os.system('cls')
    person = 'student'
    print("-" * 40)
    print("Welcome to Student Management System".center(40))
    print("-" * 40)

    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")

    ans = input("\nEnter your number of choice: ")
    if ans == '1':
        add_student()
    elif ans == '2':
        view_students(person)
    elif ans == '3':
        search_student(person)
    elif ans == '4':
        update_student()
    elif ans == '5':
        delete_student()
    elif ans == '6':
        print("-" * 40)
        print("Thank you for using our system".center(40))
        print("-" * 40)
        input("\n\nPress enter to exit . . .")
        exit()
    else:
        student_menu()


def add_student():
    os.system('cls')
    print("-" * 40)
    print("Registration Form".center(40))
    print("-" * 40)

    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("\nData saved successfully")
    ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
    if ans == 'yes':
        student_menu()
    else:
        exit()


def view_students(person):
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
                student_menu()
            else:
                faculty_menu()
        else:
            exit()
    else:
        print("\nNo enrolled students")
        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            if person == "student":
                student_menu()
            else:
                faculty_menu()
        else:
            exit()


def search_student(person):
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
                student_menu()
            else:
                faculty_menu()
        else:
            exit()
    else:
        print("\nStudent no. not found in our database")
        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            if person == "student":
                student_menu()
            else:
                faculty_menu()
        else:
            exit()


def update_student():
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
            student_menu()
        else:
            exit()
    else:
        print("\nStudent no. not found in our database")

    ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
    if ans == 'yes':
        student_menu()
    else:
        exit()


def delete_student():
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
            student_menu()
        else:
            exit()

    else:
        print("\nStudent no. not found in our database")
        ans = input("\n\nDo you want to return to main menu? [yes/no]: ").lower()
        if ans == 'yes':
            student_menu()
        else:
            exit()


# for faculty menu -------------------------------------------------------------------------------------
def faculty_member():
    os.system('cls')
    print("-" * 40)
    print("Faculty Member".center(40))
    print("-" * 40)
    print("\n[Choice 1]: Log in")
    print("[Choice 2]: Create an account")
    person = 'faculty'

    choice = input("\nEnter the number of choice: ")

    filename = "Faculty_Credentials.txt"
    if choice == "1":
        login(filename, person)

    elif choice == "2":
        signup(filename, person)

    else:
        faculty_member()


def faculty_menu():
    os.system('cls')
    print("-" * 40)
    print("Welcome to Student Management System".center(40))
    print("-" * 40)
    print("\n[Choice 1]: View students")
    print("[Choice 2]: Search students")
    print("[Choice 3]: Quit")

    person = 'faculty'
    choice = input("\nEnter the number of choice: ")
    if choice == '1':
        view_students(person)

    elif choice == '2':
        search_student(person)

    elif choice == '3':
        print("-" * 40)
        print("Thank you for using our system".center(40))
        print("-" * 40)
        input("\n\nPress enter to exit . . .")
        exit()

    else:
        faculty_menu()


# LOGIN AND CREATE ACCOUNT  -------------------------------------------------------------------------------
def signup(filename, person):
    os.system('cls')
    print("-" * 40)
    print("Create and account".center(40))
    print("-" * 40)

    file = open(filename, "a")
    file = open(filename, "r")

    email = input("\nCreate address: ")
    pwd = input("Create password: ")
    confirm_pwd = input("Confirm password: ")

    email_list = []
    pwd_list = []
    data = dict()

    if os.path.getsize(filename) > 0:
        for line in file:
            e, p = line.split(", ")
            email_list.append(e)
            pwd_list.append(p.strip())
        data = dict(zip(email_list, pwd_list))
    else:
        pass

    if confirm_pwd != pwd:
        print("Password is not same as above! \n")
        input("\n\nPress enter to retry . . .")
        signup(filename, person)

    else:
        if os.path.getsize(filename) > 0:
            if email in email_list:
                print("The email is already exist!")
                input("\n\nPress enter to retry . . .")
                signup(filename, person)

            else:
                enc = confirm_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                file = open(filename, "a")
                file.write(email + ", " + hash1 + "\n")
                file.close()

                print("You have registered successfully!")
                ans = input("\n\nDo you want to log in? [yes/no]:  ").lower()
                if ans == "yes":
                    login(filename, person)
                elif ans == "no":
                    begin()
                else:
                    pass

        else:
            enc = confirm_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            file = open(filename, "w")
            file.write(email + ", " + hash1 + "\n")
            file.close()

            print("You have registered successfully!")
            ans = input("\n\nDo you want to log in? [yes/no]:  ").lower()
            if ans == "yes":
                login(filename, person)


def login(filename, person):
    os.system('cls')
    print("-" * 40)
    print("Log in".center(40))
    print("-" * 40)

    email = input("\nEnter email address: ")
    pwd = input("Enter password: ")

    file = open(filename, "a")
    file = open(filename, "r")

    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()

    email_list = []
    pwd_list = []

    # Account does not exist
    if os.path.getsize(filename) == 0:
        print("Account does not exist!")
        ans = input("\n\nDo you want to sign up? [yes/no]: ").lower()
        if ans == "yes":
            signup(filename, person)
        elif ans == "no":
            begin()

    else:
        for line in file:
            e, p = line.split(", ")
            email_list.append(e)
            pwd_list.append(p.strip())

        data = dict(zip(email_list, pwd_list))

        # LOG IN SUCCESSFULLY
        if email in data.keys():
            if auth_hash == data[email]:
                print("Logged in Successfully!")
                input("\n\nPress enter to continue . . .")
                if person == 'student':
                    student_menu()
                elif person == 'faculty':
                    faculty_menu()

            else:
                print("Incorrect password")
                input("\n\nPress enter to retry . . .")
                login(filename, person)

        else:
            print("\nAccount does not exist!")
            ans = input("\n\nDo you want to sign up? [yes/no]: ").lower().strip()
            if ans == "yes":
                signup(filename, person)
            elif ans == "no":
                begin()
            else:
                pass


begin()
