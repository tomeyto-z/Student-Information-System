# ADD STUDENT
import csv


def add(student_data):
    student_database = 'students.csv'
    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
