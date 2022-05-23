# DATABASE TO DELETE STUDENTS
import os
import csv


def delete(student_number):
    student_database = 'students.csv'
    student_found = False
    updated_data = []

    # if the file already exist and file is not empty
    if os.path.exists(student_database) and os.path.getsize(student_database) > 0:
        with open(student_database, "r") as file:
            reader = csv.reader(file)

            # skip student if found in the row
            for row in reader:
                if student_number == row[0]:
                    student_found = True
                else:
                    updated_data.append(row)

        # rewrite the file without the skipped student
        if student_found:
            with open(student_database, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)
                return True

    # Student no. not found in our database
    return False

