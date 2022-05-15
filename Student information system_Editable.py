import os
import faculty
import student

# this is the main screen

while True:
    print("-" * 40)
    print("Welcome to Information System".center(40))
    print("-" * 40)
    print("\n[Choice 1]: Faculty member")
    print("[Choice 2]: Student")
    print("[Choice 3]: Quit")

    choice = input("\nEnter the number of choice: ")

    if choice == "1":
        faculty.member()

    elif choice == "2":
        student.member()

    elif choice == "3":
        os.system('cls')
        print("-" * 40)
        print("Thank you for using our system".center(40))
        print("-" * 40)
        input("\n\nPress enter to exit . . .")
        exit()

    else:
        os.system('cls')
        pass
