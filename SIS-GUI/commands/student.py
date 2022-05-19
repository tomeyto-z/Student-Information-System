import os
import account
import database


def member():
    os.system('cls')
    filename = "Student_Credentials.txt"
    person = 'student'

    print("-" * 40)
    print("Student module".center(40))
    print("-" * 40)
    print("\n[Choice 1]: Log in")
    print("[Choice 2]: Create an account")
    print("[Choice 3]: Back to main page")
    print("[Choice 4]: Quit")

    choice = input("\nEnter the number of choice: ")

    if choice == "1":
        account.login(filename, person)

    elif choice == "2":
        account.signup(filename, person)

    elif choice == '3':
        os.system('cls')
        return

    elif choice == '4':
        os.system('cls')
        print("-" * 40)
        print("Thank you for using our system".center(40))
        print("-" * 40)
        input("\n\nPress enter to exit . . .")
        exit()

    else:
        member()


def menu():
    os.system('cls')
    person = 'student'
    print("-" * 40)
    print("Student Management System Menu".center(40))
    print("-" * 40)

    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")

    ans = input("\nEnter your number of choice: ")
    if ans == '1':
        database.add()
    elif ans == '2':
        database.view(person)
    elif ans == '3':
        database.search(person)
    elif ans == '4':
        database.update()
    elif ans == '5':
        database.delete()
    elif ans == '6':
        os.system('cls')
        print("-" * 40)
        print("Thank you for using our system".center(40))
        print("-" * 40)
        input("\n\nPress enter to exit . . .")
        exit()
    else:
        menu()
