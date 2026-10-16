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

        # Insert the complete list of games

        writer.writerows(student_list)


def import_from_csv(filename):

    student_list = []

    try:

        with open(filename, mode='r', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            for row in reader:

                student_list.append(row)
    except FileNotFoundError:

        print(f"File '{filename}' not found. Starting with an empty student list.")

    return student_list
