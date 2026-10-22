# Main menu

# add student, show students, top 3 major grade point average, exit
import actions.functions as functions  
import data.export_students as export_students

def main ():
    student_list = []
    while True:
        print("1. Add Student")
        print("2. Show Students")
        print("3. Top 3 Major Grade Point Average")
        print("4. Show overall Average of All Students")
        print("5. Export Students to CSV")
        print("6. Import Students from CSV")
        print("7. Remove Student by name and homeroom")
        print("8. Show Failed Students")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                try:
                    amount_ofstudents = int(input("Enter the amount of students you want to add: "))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
                break
            functions.addStudent(student_list, amount_ofstudents)
        elif choice == "2":
            functions.showStudents(student_list)
        elif choice == "3":
            functions.top_3_major_grade_point_average(student_list)
        elif choice == "4":
            overall_average = functions.calculate_overall_average(student_list)
            print(f"Overall Average of All Students: {overall_average:.2f}")
        elif choice == "5":
            export_students.export_to_csv("students.csv", student_list)
        elif choice == "6":
            print("Importing students from CSV...")

            # Import the students from the csv file
            imported_students = export_students.import_from_csv("students.csv")

            # if it detects that the file is existing in the system, it will 
            # show a diffrente message
            if imported_students is not None:
                # Add the imported students to the main student list
                export_students.imported_list_to_student_list(imported_students, student_list)

                # Shows the students that were imported from the csv file
                functions.showStudents(student_list)
    
        elif choice == "7":
            functions.eliminate_student_by_name_and_homeroom(student_list)
        elif choice == "8":
            functions.show_failed_students(student_list)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")
