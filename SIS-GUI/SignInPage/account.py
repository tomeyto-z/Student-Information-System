# THIS IS THE ACCOUNT DATA BASE
import hashlib
import os


def signup(filename, email, pwd, confirm_pwd):
    file = open(filename, "a")
    file = open(filename, "r")

    email_list = []
    pwd_list = []

    if os.path.getsize(filename) > 0:
        for line in file:
            e, p = line.split(", ")
            email_list.append(e)
            pwd_list.append(p.strip())
        data = dict(zip(email_list, pwd_list))
    else:
        pass

    if confirm_pwd != pwd:
        return 2    # Password is not same as above!

    else:
        if os.path.getsize(filename) > 0:
            if email in email_list:
                return 3    # The email is already exist!

            else:
                enc = confirm_pwd.encode()
                hash1 = hashlib.md5(enc).hexdigest()
                file = open(filename, "a")
                file.write(email + ", " + hash1 + "\n")
                file.close()
                return 1    # You have registered successfully!

        else:
            enc = confirm_pwd.encode()
            hash1 = hashlib.md5(enc).hexdigest()
            file = open(filename, "w")
            file.write(email + ", " + hash1 + "\n")
            file.close()
            return 1  # You have registered successfully!


def login(filename, email, pwd):
    file = open(filename, "a")
    file = open(filename, "r")

    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()

    email_list = []
    pwd_list = []

    # If account does not exist
    if os.path.getsize(filename) == 0:
        return 2  # Account does not exist

    else:
        for line in file:
            e, p = line.split(", ")
            email_list.append(e)
            pwd_list.append(p.strip())

        data = dict(zip(email_list, pwd_list))

        # LOG IN SUCCESSFULLY
        if email in data.keys():
            if auth_hash == data[email]:
                return 1  # Logged in successfully

            else:
                return 3  # Incorrect email or password

        else:
            return 2  # Account does not exist
