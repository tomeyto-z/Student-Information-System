import os
import csv


# no return value, just pure command
def update(student_number, student_data):
    student_database = 'students.csv'
    updated_data = []

    with open(student_database, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if student_number != row[0]:
                updated_data.append(row)

        updated_data.append(student_data)

    # rewriting of database
    with open(student_database, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(updated_data)
