# DATABASE TO DELETE STUDENTS
import os
import csv


# no return statement, just command
def delete(student_number):
    student_database = 'students.csv'
    updated_data = []

    with open(student_database, "r", newline="") as file:
        reader = csv.reader(file)

        # skip student if found in the row
        for row in reader:
            if student_number == row[0]:
                student_found = True
            else:
                updated_data.append(row)

    # rewrite the file without the skipped student
    with open(student_database, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_data)

