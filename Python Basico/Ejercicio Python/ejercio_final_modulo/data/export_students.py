import actions.functions as functions 

import csv

# Method that exports all the previous methods into a CSV.

def export_to_csv(filename, student_list):

    if not student_list:

        print("No students have been added yet.")
        return

    headers = ['name', 'homeroom', 'spanish_grade', 'english_grade', 'science_grade', 'social_studies_grade']

    with open(filename, mode='w', encoding='utf-8',newline='') as file:

    # Inicializamos el escritor indicando el archivo destino y los encabezados

        writer = csv.DictWriter(file, fieldnames=headers, extrasaction='ignore')

        # write headers only if the file is new or empty

        writer.writeheader()

        # Insert the complete list of students
        writer.writerows(student_list)


def import_from_csv(filename):

    student_list = []

    try:

        with open(filename, mode='r', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            for row in reader:

                # Convert grades to float so this way there are no problems when calculating the average of the students.
                row["spanish_grade"] = float(row["spanish_grade"])
                row["english_grade"] = float(row["english_grade"])
                row["science_grade"] = float(row["science_grade"])
                row["social_studies_grade"] = float(row["social_studies_grade"])

                student_list.append(row)
    except FileNotFoundError:

        print(f"File '{filename}' not found. Starting with an empty student list.")

    return student_list

def imported_list_to_student_list(imported_list, student_list):
    imported_count = 0

    for student in imported_list:
        if not functions.has_duplicate_students(
            student_list,
            student["name"],
            student["homeroom"]
        ):
            student_list.append(student)
            imported_count += 1

    if imported_count > 0:
        print(f"{imported_count} students imported successfully.")
    else:
        print("No new students were imported. All students already exist in the main list.")

    return student_list