# THIS IS THE ACCOUNT DATA BASE

import os
import hashlib
import student
import faculty


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
                    return
                else:
                    os.system('cls')
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
            elif ans == "no":
                return
            else:
                os.system('cls')
                pass


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
            os.system('cls')
            return

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
                    student.menu()
                elif person == 'faculty':
                    faculty.menu()

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
                os.system('cls')
                return
            else:
                os.system('cls')
                pass
