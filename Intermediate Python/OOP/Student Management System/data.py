import csv
import os
from student import Student

def export_to_csv(path, students):#Option #5 Export to CSV.
    with open(path, 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Section', 'Spanish Grade', 'English Grade', 'Socials Grade', 'Science Grade'])
        for student in students:
            writer.writerow([student.student_name, student.student_section, student.spanish_grade, student.english_grade, student.socials_grade, student.science_grade])
        print("Data exported successfully.")


def import_from_csv(path, students):#Option #6 Import from CSV.
    if not os.path.exists(path):
        print("No exported file found")
    else:
        students.clear()
        with open(path, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row['Name'], row['Section'], float(row['Spanish Grade']), float(row['English Grade']), float(row['Socials Grade']), float(row['Science Grade']))
                students.append(student)
        print("Data imported successfully.")
