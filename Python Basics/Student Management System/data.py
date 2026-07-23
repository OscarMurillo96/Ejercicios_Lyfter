from actions import students
import csv
import os

def export_to_csv(path):#Option #5 Export to CSV.
    with open(path, 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Section', 'Spanish Grade', 'English Grade', 'Socials Grade', 'Science Grade'])
        for student in students:
            writer.writerow([student['name'], student['section'], student['spanish_grade'], student['english_grade'], student['socials_grade'], student['science_grade']])
        print("Data exported successfully.")


def import_from_csv(path):#Option #6 Import from CSV.
    if not os.path.exists(path):
        print("No exported file found")
    else:
        students.clear()
        with open(path, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = {
                    'name': row['Name'],
                    'section': row['Section'],
                    'spanish_grade': float(row['Spanish Grade']),
                    'english_grade': float(row['English Grade']),
                    'socials_grade': float(row['Socials Grade']),
                    'science_grade': float(row['Science Grade'])
                }
                students.append(student)
        print("Data imported successfully.")
