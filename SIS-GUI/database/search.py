import os
import csv


# return true or false weather the student is found
def search(student_number):
    student_database = 'students.csv'

    if os.path.exists(student_database) and os.path.getsize(student_database) > 0:
        with open(student_database, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if student_number == row[0]:
                    return True

            else:
                return False
    else:
        return False
