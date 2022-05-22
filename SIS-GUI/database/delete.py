# DATABASE TO DELETE STUDENTS

import os
import csv


# di ko na alam paano paikliin to HAHHAHAHAHAHA if ever na maiikli pa go lang
def delete(student_number):
    student_database = 'students.csv'
    student_found = False
    updated_data = []

    # if the file already exist and file is not empty
    if os.path.exists(student_database) and os.path.getsize(student_database) > 0:
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

            for row in reader:
                if len(row) > 0 and student_number != row[0]:
                    updated_data.append(row)
                else:
                    student_found = True

        if student_found is True:
            with open(student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
                return 1  # Student no. deleted successfully

        else:
            return 2  # Student no. not found in our database

    else:
        return 2  # Student no. not found in our database


