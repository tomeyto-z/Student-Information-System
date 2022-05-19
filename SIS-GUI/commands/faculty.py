import os
import account
import database


def member():
    os.system('cls')
    filename = "Faculty_Credentials.txt"
    person = 'faculty'

    print("-" * 40)
    print("Faculty Member".center(40))
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
    print("-" * 40)
    print("Student Management System Menu".center(40))
    print("-" * 40)
    print("\n[Choice 1]: View students")
    print("[Choice 2]: Search students")
    print("[Choice 3]: Quit")

    person = 'faculty'
    choice = input("\nEnter the number of choice: ")
    if choice == '1':
        database.view(person)

    elif choice == '2':
        database.search(person)

    elif choice == '3':
        os.system('cls')
        print("-" * 40)
        print("Thank you for using our system".center(40))
        print("-" * 40)
        input("\n\nPress enter to exit . . .")
        exit()

    else:
        menu()
