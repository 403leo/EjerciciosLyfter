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
        print("4. Export Students to CSV")
        print("5. Import Students from CSV")
        print("6. Remove Student by name and homeroom")
        print("7. Show Failed Students")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount_ofstudents = int(input("Enter the amount of students you want to add: "))
            functions.addStudent(student_list, amount_ofstudents)
        elif choice == "2":
            functions.showStudents(student_list)
        elif choice == "3":
            functions.top_3_major_grade_point_average(student_list)
        elif choice == "4":
            export_students.export_to_csv("students.csv", student_list)
        elif choice == "5":
            print("Imported students from CSV:")
            student_list1 = export_students.import_from_csv("students.csv")
            functions.showStudents(student_list1)
        elif choice == "6":
            functions.eliminate_student_by_name_and_homeroom(student_list)
        elif choice == "7":
            functions.show_failed_students(student_list)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")
