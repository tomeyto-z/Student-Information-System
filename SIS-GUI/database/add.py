# DATABASE TO ADD STUDENTS
import csv


def add(student_data):
    student_database = 'students.csv'   # the student database csv file
    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
